import asyncio
import base64
import logging
import os
import re
from typing import Dict, List, Optional, Tuple

import aiohttp
import cv2
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
from rich.logging import RichHandler
from rich.pretty import pretty_repr

import pupilcloud

# Setup the logger with a RichHandler for better visual output
logging.basicConfig(
    format="%(message)s",
    datefmt="[%X]",
    level=logging.INFO,
    handlers=[RichHandler()],
)
load_dotenv()  # Load environment variables from a .env file


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


def is_within_aoi(
    gaze_x: float, gaze_y: float, bounding_box: Dict[str, float], mask: np.ndarray
) -> bool:
    """
    Checks if a gaze point is within an Area of Interest (AOI) defined by a bounding box and a mask.
    Args:
        gaze_x (float): X-coordinate of the gaze point (relative to image width).
        gaze_y (float): Y-coordinate of the gaze point (relative to image height).
        bounding_box (dict): The bounding box of the AOI with 'min_x', 'max_x', 'min_y', 'max_y' keys.
        mask (np.ndarray): The binary mask representing the AOI.

    Returns:
        bool: True if the gaze point is within the AOI, False otherwise.
    """
    if (
        bounding_box["min_x"] <= gaze_x <= bounding_box["max_x"]
        and bounding_box["max_y"] <= gaze_y <= bounding_box["min_y"]
    ):
        h, w = mask.shape
        # Check if the point is within the non-zero region of the mask
        if np.any(mask[int(gaze_y * h), int(gaze_x * w)] != [0, 0, 0]):
            return True
        return False
    else:
        return False


async def fetch_image(url: str) -> Optional[bytes]:
    """
    Asynchronously fetches an image from a given URL.
    Args:
        url (str): The URL of the image to fetch.
    Returns:
        bytes: The raw image data if the fetch is successful, None otherwise.
    """
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
    """
    Main function to execute the asynchronous tasks, including fetching enrichment data,
    processing gaze data within AOIs, and visualizing the timeline results.
    """
    logging.getLogger("Cloud timeline")

    # Set up the Pupil Cloud API configuration
    config = pupilcloud.Configuration()
    config.api_key = {
        "workspace_id": os.environ["WORKSPACE_ID"],
        "api_key": os.environ["CLOUD_TOKEN"],
    }

    # Extract the workspace and project details from the URL
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

            # Get the reference image associated with the enrichment
            reference_image_mapper = await CloudClient.get_markerless(
                workspace_id=opts["workspace_id"],
                markerless_id=enrichment.result.additional_properties["args"][
                    "markerless_id"
                ],
            )

            # Fetch and decode the reference image
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
            list_aois: List[Dict[str, any]] = []
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

            # Initialize the plot
            fig, ax = plt.subplots(figsize=(12, 4))

            recording_height = 0
            y_labels: List[str] = []

            # Get all the slices
            aoi_legend: Dict[str, str] = {}
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

                    # Fetch gaze data for each slice
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

                    # Process and plot each gaze point
                    for gaze in gaze_data.result:
                        gaze_x = gaze.gaze_in_aoi_x
                        gaze_y = gaze.gaze_in_aoi_y
                        start_time = gaze.start_timestamp
                        end_time = gaze.end_timestamp

                        if gaze_x is not None and gaze_y is not None:
                            aoi_color = None

                            # Check which AOI the gaze falls into
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

                    # Get recording name and update labels
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
                if event.name == "recording.end"
            )
            ax.set_xlim(left=0, right=max_end_events_dur)
            ax.set_ylabel("Recordings")
            ax.set_yticks(range(len(y_labels)))
            ax.set_yticklabels(y_labels)
            ax.set_title("Gaze in AOI Over Time Across Recordings")

            # Create custom legend handles for AOIs
            handles = [
                plt.Line2D([0], [0], color=color, lw=4, label=name)
                for name, color in aoi_legend.items()
            ]
            ax.legend(handles=handles, title="AOIs")

            # Show plot and wait for the user to close it
            logging.info("Displaying the plot, close the window to continue ...")
            plt.show(block=True)

            logging.info("End")
        except pupilcloud.ApiException as e:
            logging.error(f"Exception occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
