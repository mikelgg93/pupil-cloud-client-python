import asyncio
import base64
import datetime
import logging
import os
import random
import re
import uuid
from typing import Dict, List, Optional, Tuple
from unittest.mock import patch

import aiohttp
import av
import cv2
import numpy as np
import torch
from dotenv import load_dotenv
from rich.logging import RichHandler
from transformers import AutoModelForCausalLM, AutoProcessor
from transformers.dynamic_module_utils import get_imports

import pupilcloud
from pupilcloud.models.aoi_post_request import AoiPostRequest
from pupilcloud.models.static_image_mapper_post_request import (
    StaticImageMapperPostRequest,
)


def fixed_get_imports(filename: str | os.PathLike) -> list[str]:
    if not str(filename).endswith("modeling_florence2.py"):
        return get_imports(filename)
    imports = get_imports(filename)
    imports.remove("flash_attn")
    return imports


# Setup the logger with a RichHandler for better visual output
logging.basicConfig(
    format="%(message)s",
    datefmt="[%X]",
    level=logging.INFO,
    handlers=[RichHandler()],
)
load_dotenv()  # Load environment variables from a .env file

# Settign up the inference model.
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
model_id = "microsoft/Florence-2-large"
with patch(
    "transformers.dynamic_module_utils.get_imports", fixed_get_imports
):  # workaround for unnecessary flash_attn requirement
    model = AutoModelForCausalLM.from_pretrained(
        model_id, torch_dtype=torch_dtype, trust_remote_code=True
    ).to(device)

processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
task_prompt = "<OPEN_VOCABULARY_DETECTION>"
# "<OD>"  # for generic object detection,
#'<REFERRING_EXPRESSION_SEGMENTATION>' for segmentation

# For more examples of Florence-2, head to
# https://huggingface.co/microsoft/Florence-2-large/blob/main/sample_inference.ipynb


def extract_from_url(url: str) -> Tuple[str, Dict[str, Optional[str]]]:
    """
    Extracts the base URL and specific segments (IDs) from a given Cloud URL.
    Args:
        url (str): The full URL to extract from.
    Returns:
        tuple: Base URL and a dictionary of extracted segments.
    """
    base_url = re.match(r"https?://[^/]+", url).group(0)

    segments = {
        "workspace_id": "/workspaces/",
        "project_id": "/projects/",
        "enrichment_id": "/enrichments/",
        "recording_id": "/recordings/",
        "wearer_id": "/wearers/",
        "event_id": "/events/",
        "fixation_id": "/fixations/",
    }

    extracted_segments = {}

    for key, segment in segments.items():
        match = re.search(f"{segment}([^/]+)", url)
        if match:
            extracted_segments[key] = match.group(1)
        else:
            extracted_segments[key] = None

    return base_url, extracted_segments


def generate_reference_image(
    obj2find: List[str],
) -> Tuple[np.ndarray, Dict[str, Dict[str, Tuple[int, int]]]]:
    """
    Generate a reference image with the specified words and their bounding boxes and centroids.
    Args:
        obj2find (List[str]): List of words to be placed on the image.
    Returns:
        Tuple[np.ndarray, Dict[str, Dict[str, Tuple[int, int]]]]:
        The generated reference image and a dictionary containing the bounding boxes and centroids for each word.
    """

    def generate_random_color_hex() -> Tuple[int, int, int]:
        """Generate a random color in RGB format."""
        hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))[::-1]

    def encode_image_to_base64(image: np.ndarray) -> str:
        """Encode an image to a base64 string."""
        _, buffer = cv2.imencode(".png", image)
        return base64.b64encode(buffer).decode("utf-8")

    image_size = 1024
    ref_image = np.ones((image_size, image_size, 3), dtype=np.uint8) * 255
    bbox_locations: Dict[str, Dict[str, Tuple[int, int]]] = {}
    offset = 100

    for i, word in enumerate(obj2find):
        text_size = cv2.getTextSize(
            word, cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, thickness=3
        )[0]
        text_x = (image_size - text_size[0]) // 2
        text_y = offset + i * (text_size[1] + offset)
        cv2.putText(
            ref_image,
            word,
            (text_x, text_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=2,
            color=(0, 0, 0),
            thickness=3,
            lineType=cv2.LINE_AA,
        )
        x_min, y_min = text_x, text_y - text_size[1]
        x_max, y_max = text_x + text_size[0], text_y
        centroid_x = (x_min + x_max) // 2
        centroid_y = (y_min + y_max) // 2
        mask = np.zeros((image_size, image_size), dtype=np.uint8)
        mask[y_min:y_max, x_min:x_max] = 1

        color = generate_random_color_hex()
        colored_mask = np.zeros((*mask.shape, 4), dtype=np.uint8)
        colored_mask[mask == 1] = color + (255,)
        colored_mask[mask == 0] = (0, 0, 0, 0)

        encoded_mask = encode_image_to_base64(colored_mask)
        bbox = {
            "word": word,
            "x_min": text_x,
            "y_min": text_y - text_size[1],
            "x_max": text_x + text_size[0],
            "y_max": text_y,
            "centroid": (centroid_x, centroid_y),
            "mask": f"data:image/png;base64,{encoded_mask}",
        }
        bbox_locations[word] = bbox

    return ref_image, bbox_locations


async def upload_image_to_cloud(
    workspace_id: str, api_key: str, image: np.ndarray, file_name: str
) -> Optional[str]:
    """
    Uploads an image to the Pupil Labs Cloud using the Tus protocol.

    Args:
        workspace_id (str): The workspace ID for the Pupil Labs Cloud.
        api_key (str): The API key for authentication.
        image_data (bytes): The image data as bytes.
        file_name (str): The name of the file as it will be saved on the server.

    Returns:
        Optional[str]: The URL of the uploaded file if successful, otherwise None.
    """
    url = f"https://api.cloud.pupil-labs.com/v2/workspaces/{workspace_id}/files/"

    filename_base64 = base64.b64encode(file_name.encode("utf-8")).decode("utf-8")
    content_type_base64 = base64.b64encode(b"image/jpeg").decode("utf-8")

    _, image_encoded = cv2.imencode(".jpg", image)
    image_base64 = base64.b64encode(image_encoded).decode("utf-8")

    filename_base64 = base64.b64encode(file_name.encode("utf-8")).decode("utf-8")
    content_type_base64 = base64.b64encode(b"image/png").decode("utf-8")
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "api-key": api_key,
        "workspace-id": workspace_id,
        "Tus-Resumable": "1.0.0",
        "Upload-Length": str(len(image_base64)),
        "Upload-Metadata": f"name {filename_base64},content_type {content_type_base64}",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers) as response:
            if response.status == 201:
                response_json = await response.json()
                upload_url = response_json["result"]["upload_url"]
                file_id = response_json["result"]["id"]
            else:
                error_message = await response.text()
                logging.error(
                    f"Failed to initiate upload. Status code: {response.status}. Error: {error_message}"
                )
                return None

        headers = {
            "Tus-Resumable": "1.0.0",
            "Content-Type": "application/offset+octet-stream",
            "Upload-Offset": "0",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "api-key": api_key,
            "workspace-id": workspace_id,
        }

        async with session.patch(
            upload_url, headers=headers, data=image_base64
        ) as response:
            if response.status == 204:
                return file_id
            else:
                error_message = await response.text()
                logging.error(
                    f"Failed to upload file data. Status code: {response.status}. Error: {error_message}"
                )
                return None


async def get_scene_video_container(
    api_key: str,
    workspace_id: str,
    recording_id: str,
) -> Optional[av.container.InputContainer]:
    """
    Constructs the scene video URL, fetches the video stream, and returns it as an AV container.

    Args:
        api_key (str): The API key for authentication.
        workspace_id (str): Workspace ID.
        recording_id (str): Recording ID.

    Returns:
        Optional[av.container.InputContainer]: The AV container with the video stream, or None if the request fails.
    """
    endpoint = f"https://api.cloud.pupil-labs.com/v2/workspaces/{workspace_id}/recordings/{recording_id}/files/scene.mp4?cbw="
    headers = {
        "api-key": api_key,
        "workspace-id": workspace_id,
        "Accept": "*/*",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(
            endpoint, headers=headers, allow_redirects=True
        ) as response:
            if response.status == 200:
                container = av.open(str(response.url))
                return container
            else:
                print(f"Failed to get scene video. Status code: {response.status}")
                return None


def seek_closest_frame(
    container: av.container.InputContainer, seek_time: float
) -> Optional[av.VideoFrame]:
    """
    Seeks to the closest video frame at or after the specified time in the given container.

    Args:
        container (av.container.InputContainer): The AV container containing the video stream.
        seek_time (float): The time (in seconds) to seek to within the video.

    Returns:
        Optional[av.VideoFrame]: The closest video frame at or after the specified time, or None if not found.
    """
    stream = next(s for s in container.streams if s.type == "video")
    time_base = stream.time_base
    target_pts = int(seek_time / float(time_base))

    container.seek(offset=target_pts, stream=stream, any_frame=False)

    for frame in container.decode(video=0):
        frame_timestamp = frame.pts * float(time_base)

        if frame_timestamp >= seek_time:
            return frame

    return None


def florence_inference(
    image, task_prompt: str, text_input: Optional[str] = None
) -> str:
    """
    Performs inference using the Florence model based on the given image and task prompt.

    Args:
        image: The input image for the model.
        task_prompt (str): The prompt describing the task for the model.
        text_input (Optional[str]): Additional text input to append to the task prompt. Defaults to None.

    Returns:
        str: The parsed answer generated by the model.
    """
    if text_input is None:
        prompt = task_prompt
    else:
        prompt = task_prompt + text_input

    inputs = processor(text=prompt, images=image, return_tensors="pt").to(
        device, torch_dtype
    )

    generated_ids = model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        num_beams=3,
        do_sample=False,
    )

    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]

    parsed_answer = processor.post_process_generation(
        generated_text, task=task_prompt, image_size=(image.shape[1], image.shape[0])
    )

    return parsed_answer


async def main():
    """
    Main function to execute the asynchronous tasks, including fetching the project,
    creating the manual mapper enrichment, generating the semantic map and uploading the image,
    fetching the fixation and frames, processing them with Florence-2 and returning it.
    """
    logging.getLogger("Cloud Semantic Mapping")

    # Set up the Pupil Cloud API configuration
    config = pupilcloud.Configuration()
    config.api_key = {
        "workspace_id": os.environ["WORKSPACE_ID"],
        "api_key": os.environ["CLOUD_TOKEN"],
    }

    # Extract the workspace and project details from the URL
    _, opts = extract_from_url(os.environ["URL"])

    # Objects to find:
    obj2find = ["car", "phone", "flag", "building"]

    # Generate the Semantic Word Map
    ref_image, words_bbox = generate_reference_image(obj2find)

    async with pupilcloud.ApiClient(config) as api_client:
        CloudClient = pupilcloud.CloudClientApi(api_client)
        logging.info(CloudClient)

        try:
            # Fetch the project
            project = await CloudClient.get_project_resource(
                workspace_id=opts["workspace_id"], project_id=opts["project_id"]
            )
            logging.info(f"Project: {project.result.name}")
            # Fetch unique events in the project
            events = await CloudClient.get_project_events_resource(
                workspace_id=opts["workspace_id"], project_id=opts["project_id"]
            )
            # Set the events start and end
            start_event = "recording.begin"
            end_event = "recording.end"

            # Check if events are in, else return
            if not any(event.name == start_event for event in events.result) or not any(
                event.name == end_event for event in events.result
            ):
                logging.error(
                    f"Required events '{start_event}' or '{end_event}' are missing. Exiting."
                )
                return

            # Upload image
            ref_image_id = await upload_image_to_cloud(
                workspace_id=opts["workspace_id"],
                api_key=os.environ["CLOUD_TOKEN"],
                image=ref_image,
                file_name="semantic_map.jpg",
            )
            if not ref_image_id:
                return

            # Create the Manual Mapper Enrichment payload
            ManualMapperPayload = StaticImageMapperPostRequest(
                from_event_name=start_event,
                to_event_name=end_event,
                static_image_id=ref_image_id,
                name="Semantic Mapper",
            )

            # Create the Manual Mapper Enrichment
            manual_mapper = await CloudClient.post_static_image_mapper_enrichment(
                workspace_id=opts["workspace_id"],
                project_id=opts["project_id"],
                payload=ManualMapperPayload,
            )
            if manual_mapper is None:
                enrichments = await CloudClient.get_project_enrichments(
                    workspace_id=opts["workspace_id"],
                    project_id=opts["project_id"],
                )
                for enrichment in enrichments.result:
                    if enrichment.additional_properties["name"] == "Semantic Mapper":
                        opts["enrichment_id"] = enrichment.additional_properties["id"]
                        manual_mapper = (
                            await CloudClient.get_static_image_mapper_enrichment(
                                workspace_id=opts["workspace_id"],
                                project_id=opts["project_id"],
                                static_enrichment_id=enrichment.additional_properties[
                                    "id"
                                ],
                            )
                        )

            # Now, lets go through the slices
            for i, slice in enumerate(manual_mapper.result.slices):
                # Get the video to pyav
                container = await get_scene_video_container(
                    workspace_id=opts["workspace_id"],
                    api_key=os.environ["CLOUD_TOKEN"],
                    recording_id=slice["recording_id"],
                )

                # Get the fixations to map:
                fixations = await CloudClient.get_static_image_mapper_enrichments_recording_fixations(
                    workspace_id=opts["workspace_id"],
                    project_id=opts["project_id"],
                    enrichment_id=opts["enrichment_id"],
                    recording_id=slice["recording_id"],
                )

                for fixation in fixations.result.fixations:
                    logging.info(
                        f"Fixation: {fixation['fixation_id']} out of {fixations.result.total_fixations} (rec.{i} out of {len(manual_mapper.result.slices)})"
                    )
                    fixated_object = []
                    # Get the frame for the fixation
                    seek_time = fixation["seek_timestamp"]
                    frame = seek_closest_frame(container, seek_time)
                    scene_img = frame.to_ndarray(format="bgr24")
                    img = scene_img.copy()

                    # Get fixation on the scene camera
                    original_fixations = await CloudClient.get_recording_scanpath(
                        workspace_id=opts["workspace_id"],
                        recording_id=slice["recording_id"],
                        format="json",
                        start=seek_time - 0.033,
                        end=seek_time + 0.033,
                        max_length=1,
                    )
                    matching_entries = [
                        item
                        for item in original_fixations.result
                        if item.start_timestamp <= seek_time <= item.end_timestamp
                    ]
                    if matching_entries:
                        ms, x, y = (
                            matching_entries[0].path[-1][key]
                            for key in ("ms", "x", "y")
                        )
                    # Inference on the image with the prompts
                    bboxes, labels = [], []
                    for obj in obj2find:
                        objs_detected = florence_inference(
                            image=scene_img,
                            task_prompt=task_prompt,
                            text_input=obj,
                        )
                        bboxes.extend(objs_detected[task_prompt]["bboxes"])
                        labels.extend(objs_detected[task_prompt]["bboxes_labels"])

                    # Show with OpenCV the frame the bboxes, fixation and label fixated
                    # together with the reference image.
                    for bbox, label in zip(bboxes, labels):
                        r_img = ref_image.copy()
                        x_min, y_min, x_max, y_max = map(int, bbox)
                        if x_min <= x <= x_max and y_min <= y <= y_max:
                            fixated_object.append(label)
                            cv2.rectangle(
                                r_img,
                                (
                                    words_bbox[label]["x_min"],
                                    words_bbox[label]["y_min"],
                                ),
                                (
                                    words_bbox[label]["x_max"],
                                    words_bbox[label]["y_max"],
                                ),
                                color=(0, 255, 0),
                                thickness=2,
                            )

                        cv2.rectangle(
                            img,
                            (x_min, y_min),
                            (x_max, y_max),
                            color=(0, 255, 0),
                            thickness=2,
                        )
                        label_text = f"{label}"
                        label_position = (x_min, y_min - 10)
                        cv2.putText(
                            img,
                            label_text,
                            label_position,
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,
                            (0, 255, 0),
                            2,
                        )
                    cv2.circle(img, (x, y), radius=10, color=(255, 0, 0), thickness=5)

                    # If fixation on bounding box on any of them
                    # send it to to the centroid of the bbox of that label
                    if fixated_object:
                        img_height, _ = img.shape[:2]
                        r_img_height, r_img_width = r_img.shape[:2]
                        if img_height != r_img_height:
                            r_img = cv2.resize(r_img, (r_img_width, img_height))
                        cv2.imshow("Image with Bounding Boxes", np.hstack((img, r_img)))
                        cv2.waitKey(1)
                        fixation_point_submitted = await CloudClient.put_static_image_mapper_enrichments_recording_fixation(
                            workspace_id=opts["workspace_id"],
                            project_id=opts["project_id"],
                            enrichment_id=opts["enrichment_id"],
                            recording_id=slice["recording_id"],
                            fixation_id=fixation["fixation_id"],
                            payload={
                                "gaze_on_aoi": 1,
                                "x": words_bbox[fixated_object[0]]["centroid"][0]
                                / r_img_width,
                                "y": words_bbox[fixated_object[0]]["centroid"][1]
                                / r_img_height,
                            },
                        )
                    else:
                        fixation_point_submitted = await CloudClient.put_static_image_mapper_enrichments_recording_fixation(
                            workspace_id=opts["workspace_id"],
                            project_id=opts["project_id"],
                            enrichment_id=opts["enrichment_id"],
                            recording_id=slice["recording_id"],
                            fixation_id=fixation["fixation_id"],
                            payload={
                                "gaze_on_aoi": 0,
                                "x": None,
                                "y": None,
                            },
                        )
                    logging.info(fixation_point_submitted)

            # Now create the AOIs with the bboxes
            for object in words_bbox:
                aoi_payload = AoiPostRequest(
                    name=object["name"],
                    created_at=datetime.utcnow().isoformat() + "Z",
                    description="string",
                    enrichment_id=opts["enrichment_id"],
                    id=str(uuid.uuid4()),
                    mask_image_data_url=object["mask"],
                )
                aoi_submitted = await CloudClient.post_aoi(
                    workspace_id=opts["workspace_id"],
                    project_id=opts["project_id"],
                    enrichment_id=opts["enrichment_id"],
                    payload=aoi_payload,
                )
                logging.info(aoi_submitted)

        except pupilcloud.ApiException as e:
            logging.error(f"Exception occurred: {e}")

    logging.info("Ended")


if __name__ == "__main__":
    asyncio.run(main())
