import asyncio
import logging
import math
import os
import re
from typing import Dict, Optional, Tuple

import aiohttp
import av
import numpy as np
from dotenv import load_dotenv
from rich.logging import RichHandler

import pupilcloud
from examples.circle_detector.circle_detector import CircleTracker

# Setup the logger with a RichHandler for better visual output
logging.basicConfig(
    format="%(message)s",
    datefmt="[%X]",
    level=logging.INFO,
    handlers=[RichHandler()],
)
load_dotenv()  # Load environment variables from a .env file

tracker = CircleTracker()


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
    endpoint = f"https://api.cloud.pupil-labs.dev/v2/workspaces/{workspace_id}/recordings/{recording_id}/files/scene.mp4?cbw="
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


async def main():
    """
    Main function to execute the asynchronous tasks, including fetching recording data,
    processing gaze data and the frame to detect the marker, and setting a new offset correction.
    """
    logging.getLogger("Cloud timeline")

    # Set up the Pupil Cloud API configuration
    config = pupilcloud.Configuration(host=os.environ["HOST"])
    config.api_key = {
        "workspace_id": os.environ["WORKSPACE_ID"],
        "api_key": os.environ["CLOUD_TOKEN"],
    }

    # Extract the workspace and project details from the URL
    _, opts = extract_from_url(os.environ["URL"])

    # Set the recording ID
    opts["recording_id"] = "eae4c514-621c-48a2-8917-86ea5becde37"

    async with pupilcloud.ApiClient(config) as api_client:
        CloudClient = pupilcloud.CloudClientApi(api_client)
        logging.info(CloudClient)

        try:
            # Fetch recording
            recording = await CloudClient.get_recording(
                workspace_id=opts["workspace_id"], recording_id=opts["recording_id"]
            )
            logging.info(
                f"Rec: {recording.result.name} recorded at {recording.result.recorded_at}"
            )
            logging.info(
                f"with gaze offset on the App: {recording.result.android_gaze_offset}"
            )
            logging.info(f"with gaze offset in Cloud: {recording.result.gaze_offset}")
            container = await get_scene_video_container(
                workspace_id=opts["workspace_id"],
                api_key=os.environ["CLOUD_TOKEN"],
                recording_id=opts["recording_id"],
            )

            # Fetch events
            events = await CloudClient.get_recording_events(
                workspace_id=opts["workspace_id"],
                recording_id=opts["recording_id"],
            )
            # Set the events start and end
            start_event = "calibration.start"
            end_event = "calibration.end"

            # Check if events are in, else return
            if not any(event.name == start_event for event in events.result) or not any(
                event.name == end_event for event in events.result
            ):
                logging.error(
                    f"Required events '{start_event}' or '{end_event}' are missing. Exiting."
                )
                return
            else:
                start_event = next(
                    (event for event in events.result if event.name == start_event),
                    None,
                )
                end_event = next(
                    (event for event in events.result if event.name == end_event),
                    None,
                )

            # For event A to B iterate throught the frames detecting marker position
            num_steps = int((end_event.offset_s - start_event.offset_s) / 0.033) + 1
            logging.info(f"Time calib: {end_event.offset_s - start_event.offset_s} sec")
            logging.info(
                f"Potential frames {num_steps}, potential gaze points ({num_steps*200})"
            )

            points = []
            for ts in np.linspace(start_event.offset_s, end_event.offset_s, num_steps):
                # Fetch frame:
                frame = seek_closest_frame(container, ts)

                # Fetch gaze
                gazes = await CloudClient.get_recording_gaze(
                    workspace_id=opts["workspace_id"],
                    recording_id=opts["recording_id"],
                    start=ts,
                    end=ts + 0.033,
                    max_length=1,
                    format="json",
                )

                # Detect marker
                markers = tracker.update(img=frame.to_ndarray(format="gray"))
                ref_marker = None
                for marker in markers:
                    if marker["marker_type"] == "Ref":
                        ref_marker = marker

                if ref_marker is None:
                    continue

                x_marker, y_marker = ref_marker["img_pos"]
                for gaze in gazes.result:
                    if gaze.blink_id is None:
                        points.append(
                            {
                                "ts": gaze.start_timestamp,
                                "x_marker": x_marker,
                                "y_marker": y_marker,
                                "x_gaze": gaze.x,
                                "y_gaze": gaze.y,
                                "euclidean_distance_with_offset": math.sqrt(
                                    (x_marker - gaze.x) ** 2 + (y_marker - gaze.y) ** 2
                                ),
                                "x_diff": x_marker - gaze.x,
                                "y_diff": y_marker - gaze.y,
                                "euclidean_distance_without_offset": math.sqrt(
                                    (
                                        x_marker
                                        - (gaze.x - recording.result.gaze_offset.x)
                                    )
                                    ** 2
                                    + (
                                        y_marker
                                        - (gaze.y - recording.result.gaze_offset.y)
                                    )
                                    ** 2
                                ),
                                "x_diff_without_offset": x_marker
                                - (gaze.x - recording.result.gaze_offset.x),
                                "y_diff_without_offset": y_marker
                                - (gaze.y - recording.result.gaze_offset.y),
                            }
                        )

            # Compute distance from gaze to marker
            logging.info(f"{len(points)} points used.")

            # Compute the mean of x_diff and y_diff
            mean_x_diff = np.mean(np.array([point["x_diff"] for point in points]))
            mean_y_diff = np.mean(np.array([point["y_diff"] for point in points]))

            mean_x_diff_without_offset = np.mean(
                np.array([point["x_diff_without_offset"] for point in points])
            )
            mean_y_diff_without_offset = np.mean(
                np.array([point["y_diff_without_offset"] for point in points])
            )

            mean_euclidean = np.mean(
                np.array([point["euclidean_distance_with_offset"] for point in points])
            )
            mean_euclidean_without_offset = np.mean(
                np.array(
                    [point["euclidean_distance_without_offset"] for point in points]
                )
            )
            logging.info(
                f"Mean without offset: {mean_x_diff_without_offset, mean_y_diff_without_offset}"
            )
            logging.info(f"Mean estimated with offset: {mean_x_diff, mean_y_diff}")

            logging.info(
                f"""Mean distance from gaze to target with offset: {mean_euclidean}, 
                without {mean_euclidean_without_offset}"""
            )
            # Validate
            start_event = "validation.start"
            end_event = "validation.end"

            # Check if events are in, else return
            if not any(event.name == start_event for event in events.result) or not any(
                event.name == end_event for event in events.result
            ):
                logging.error(
                    f"Required events '{start_event}' or '{end_event}' are missing. Exiting."
                )
                return
            else:
                start_event = next(
                    (event for event in events.result if event.name == start_event),
                    None,
                )
                end_event = next(
                    (event for event in events.result if event.name == end_event),
                    None,
                )

            # For event A to B iterate throught the frames detecting marker position
            num_steps = int((end_event.offset_s - start_event.offset_s) / 0.033) + 1
            logging.info(
                f"Time validation: {end_event.offset_s - start_event.offset_s} sec"
            )
            logging.info(
                f"Potential frames {num_steps}, potential gaze points ({num_steps*200})"
            )

            points = []
            for ts in np.linspace(start_event.offset_s, end_event.offset_s, num_steps):
                # Fetch frame:
                frame = seek_closest_frame(container, ts)

                # Fetch gaze
                gazes = await CloudClient.get_recording_gaze(
                    workspace_id=opts["workspace_id"],
                    recording_id=opts["recording_id"],
                    start=ts,
                    end=ts + 0.033,
                    max_length=1,
                    format="json",
                )

                # Detect marker
                markers = tracker.update(img=frame.to_ndarray(format="gray"))
                ref_marker = None

                for marker in markers:
                    if marker["marker_type"] == "Ref":
                        ref_marker = marker

                if ref_marker is None:
                    continue

                x_marker, y_marker = ref_marker["img_pos"]
                for gaze in gazes.result:
                    if gaze.blink_id is None:
                        points.append(
                            {
                                "ts": gaze.start_timestamp,
                                "x_marker": x_marker,
                                "y_marker": y_marker,
                                "x_gaze": gaze.x,
                                "y_gaze": gaze.y,
                                "euclidean_distance_with_offset": math.sqrt(
                                    (x_marker - gaze.x) ** 2 + (y_marker - gaze.y) ** 2
                                ),
                                "x_diff": x_marker - gaze.x,
                                "y_diff": y_marker - gaze.y,
                                "euclidean_distance_without_offset": math.sqrt(
                                    (
                                        x_marker
                                        - (gaze.x - recording.result.gaze_offset.x)
                                    )
                                    ** 2
                                    + (
                                        y_marker
                                        - (gaze.y - recording.result.gaze_offset.y)
                                    )
                                    ** 2
                                ),
                                "x_diff_without_offset": x_marker
                                - (gaze.x - recording.result.gaze_offset.x),
                                "y_diff_without_offset": y_marker
                                - (gaze.y - recording.result.gaze_offset.y),
                                "euclidean_distance_with_new_offset": math.sqrt(
                                    (
                                        x_marker
                                        - (
                                            gaze.x
                                            - recording.result.gaze_offset.x
                                            + mean_x_diff_without_offset
                                        )
                                    )
                                    ** 2
                                    + (
                                        y_marker
                                        - (
                                            gaze.y
                                            - recording.result.gaze_offset.y
                                            + mean_y_diff_without_offset
                                        )
                                    )
                                    ** 2
                                ),
                                "x_diff_with_new_offset": x_marker
                                - (
                                    gaze.x
                                    - recording.result.gaze_offset.x
                                    + mean_x_diff_without_offset
                                ),
                                "y_diff_with_new_offset": y_marker
                                - (
                                    gaze.y
                                    - recording.result.gaze_offset.y
                                    + mean_y_diff_without_offset
                                ),
                            }
                        )
            # Compute distance from gaze to marker
            logging.info(f"{len(points)} points used.")

            # Compute the mean of x_diff and y_diff
            mean_x_diff = np.mean(np.array([point["x_diff"] for point in points]))
            mean_y_diff = np.mean(np.array([point["y_diff"] for point in points]))

            mean_x_diff_without_offset = np.mean(
                np.array([point["x_diff_without_offset"] for point in points])
            )
            mean_y_diff_without_offset = np.mean(
                np.array([point["y_diff_without_offset"] for point in points])
            )

            mean_x_diff_with_new_offset = np.mean(
                np.array([point["x_diff_with_new_offset"] for point in points])
            )
            mean_y_diff_with_new_offset = np.mean(
                np.array([point["y_diff_with_new_offset"] for point in points])
            )

            mean_euclidean = np.mean(
                np.array([point["euclidean_distance_with_offset"] for point in points])
            )
            mean_euclidean_without_offset = np.mean(
                np.array(
                    [point["euclidean_distance_without_offset"] for point in points]
                )
            )
            mean_euclidean_with_new_offset = np.mean(
                np.array(
                    [point["euclidean_distance_with_new_offset"] for point in points]
                )
            )

            logging.info(
                f"Mean estimated without offset: {mean_x_diff_without_offset, mean_y_diff_without_offset}"
            )
            logging.info(
                f"Mean estimated with current offset: {mean_x_diff, mean_y_diff}"
            )

            logging.info(
                f"Mean estimated with new offset: {mean_x_diff_with_new_offset, mean_y_diff_with_new_offset}"
            )
            logging.info(
                f"""Mean distance from gaze to target with offset: {mean_euclidean}, 
                without {mean_euclidean_without_offset}
                with new defined offset {mean_euclidean_with_new_offset}"""
            )
            # Apply offset
            logging.info("End")
        except pupilcloud.ApiException as e:
            logging.error(f"Exception occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
