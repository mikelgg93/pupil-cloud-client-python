import asyncio
import base64
import logging
import os
import re

import aiohttp
import cv2
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
from rich.logging import RichHandler
from rich.pretty import pretty_repr

import pupilcloud

# Setup the logger
logging.basicConfig(
    format="%(message)s",
    datefmt="[%X]",
    level=logging.INFO,
    handlers=[RichHandler()],
)
load_dotenv()


def extract_from_url(url: str) -> dict:
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


def is_within_aoi(gaze_x, gaze_y, bounding_box, mask):
    if (
        bounding_box["min_x"] <= gaze_x <= bounding_box["max_x"]
        and bounding_box["max_y"] <= gaze_y <= bounding_box["min_y"]
    ):
        h, w = mask.shape
        if np.any(mask[int(gaze_y * h), int(gaze_x * w)] != [0, 0, 0]):
            return True
        return False
    else:
        return False


async def fetch_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = await response.read()
                return image_data
            else:
                logging.error(
                    f"Failed to load the image. Status code: {response.status}"
                )
                return None


async def main():
    logging.getLogger("Cloud timeline")

    config = pupilcloud.Configuration()
    config.api_key = {
        "workspace_id": os.environ["WORKSPACE_ID"],
        "api_key": os.environ["CLOUD_TOKEN"],
    }

    _, opts = extract_from_url(os.environ["URL"])

    async with pupilcloud.ApiClient(config) as api_client:
        CloudClient = pupilcloud.CloudClientApi(api_client)
        logging.info(CloudClient)
        try:
            # Get enrichment data
            enrichment = await CloudClient.get_project_enrichment(
                workspace_id=opts["workspace_id"],
                project_id=opts["project_id"],
                enrichment_id=opts["enrichment_id"],
            )
            logging.info(pretty_repr(enrichment.result))

            # Get reference image
            reference_image_mapper = await CloudClient.get_markerless(
                workspace_id=opts["workspace_id"],
                markerless_id=enrichment.result.additional_properties["args"][
                    "markerless_id"
                ],
            )

            image_data = await fetch_image(
                reference_image_mapper.result.reference_image_thumbnail_url
            )
            if image_data:
                image_array = np.frombuffer(image_data, np.uint8)
                ref_image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
            else:
                return

            h, w, _ = ref_image.shape

            # Get AOIs (Areas of Interest)
            aois = await CloudClient.get_aois(
                workspace_id=opts["workspace_id"],
                project_id=opts["project_id"],
                enrichment_id=opts["enrichment_id"],
            )
            list_aois = []
            for aoi in aois.result:
                aoi_formatted = {
                    "name": aoi.name,
                    "bounding_box": aoi.bounding_box,
                    "mask": cv2.imdecode(
                        np.frombuffer(
                            base64.b64decode(aoi.mask_image_data_url.split(",")[1]),
                            dtype=np.uint8,
                        ),
                        cv2.IMREAD_GRAYSCALE,
                    ),
                    "color": aoi.color,
                }
                list_aois.append(aoi_formatted)

            fig, ax = plt.subplots(figsize=(12, 4))

            recording_height = 0
            y_labels = []

            # Filter out slices not matching the current recording ID
            aoi_legend = {}
            for i, slice in enumerate(
                enrichment.result.additional_properties["slices"]
            ):
                if (
                    slice["recording_id"]
                    != reference_image_mapper.result.scanning_recording_id
                ):
                    logging.info(
                        f"{i} out of {len(enrichment.result.additional_properties['slices'])}"
                    )
                    gaze_data = await CloudClient.get_markerless_gaze_on_aoi(
                        workspace_id=opts["workspace_id"],
                        project_id=opts["project_id"],
                        enrichment_id=opts["enrichment_id"],
                        markerless_id=enrichment.result.additional_properties["args"][
                            "markerless_id"
                        ],
                        recording_id=slice["recording_id"],
                        start=slice["start_time_s"],
                        end=slice["end_time_s"],
                    )

                    for gaze in gaze_data.result:
                        gaze_x = gaze.gaze_in_aoi_x
                        gaze_y = gaze.gaze_in_aoi_y
                        start_time = gaze.start_timestamp
                        end_time = gaze.end_timestamp

                        if gaze_x is not None and gaze_y is not None:
                            aoi_color = None

                            for aoi in list_aois:
                                if is_within_aoi(
                                    gaze_x, gaze_y, aoi["bounding_box"], aoi["mask"]
                                ):
                                    if aoi_color is None:
                                        aoi_color = aoi["color"]
                                        if aoi["name"] not in aoi_legend:
                                            aoi_legend[aoi["name"]] = aoi_color
                                    else:
                                        aoi_color = "white"

                            bar_color = aoi_color if aoi_color else "black"
                        else:
                            bar_color = "black"

                        ax.barh(
                            y=recording_height,
                            width=end_time - start_time,
                            left=start_time,
                            color=bar_color,
                        )
                    recording = await CloudClient.get_recording(
                        workspace_id=opts["workspace_id"],
                        recording_id=slice["recording_id"],
                    )
                    y_labels.append(f"{recording.result.name}")
                    recording_height += 1

            # Set plot labels and title
            ax.set_xlabel("Time (s)")
            events = await CloudClient.get_project_events_resource(
                workspace_id=opts["workspace_id"], project_id=opts["project_id"]
            )
            max_end_events_dur = max(
                event.offset_s
                for event in events.result
                if (event.name == "recording.end")
            )
            ax.set_xlim(left=0, right=max_end_events_dur)
            ax.set_ylabel("Recordings")
            ax.set_yticks(range(len(y_labels)))
            ax.set_yticklabels(y_labels)
            ax.set_title("Gaze in AOI Over Time Across Recordings")

            # Create custom legend handles
            handles = [
                plt.Line2D([0], [0], color=color, lw=4, label=name)
                for name, color in aoi_legend.items()
            ]
            ax.legend(handles=handles, title="AOIs")

            # Show plot
            logging.info("Displaying the plot, close the window to continue ...")
            plt.show(block=True)

            logging.info("End")
        except pupilcloud.ApiException as e:
            logging.error(f"Exception occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
