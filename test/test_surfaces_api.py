# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.surfaces_api import SurfacesApi


class TestSurfacesApi(unittest.TestCase):
    """SurfacesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SurfacesApi()

    def tearDown(self) -> None:
        pass

    def test_get_apriltag_detections(self) -> None:
        """Test case for get_apriltag_detections

        Get apritag data for surface enrichment
        """
        pass

    def test_get_surface(self) -> None:
        """Test case for get_surface

        Return surface definition
        """
        pass

    def test_get_surface_corners(self) -> None:
        """Test case for get_surface_corners

        get surface locations for surface enrichment
        """
        pass

    def test_get_surface_detections_timeline(self) -> None:
        """Test case for get_surface_detections_timeline

        Recording surface detections
        """
        pass

    def test_get_surface_gaze_on_aoi(self) -> None:
        """Test case for get_surface_gaze_on_aoi

        get gaze on aoi data for markerless enrichment
        """
        pass

    def test_patch_rotate_surface_orientation(self) -> None:
        """Test case for patch_rotate_surface_orientation

        Change surface rotation
        """
        pass

    def test_patch_surface(self) -> None:
        """Test case for patch_surface

        Update surface definition
        """
        pass

    def test_post_distorted_surface_location(self) -> None:
        """Test case for post_distorted_surface_location

        Set distorted surface corner locations
        """
        pass

    def test_post_surface(self) -> None:
        """Test case for post_surface

        Create a new surface definition
        """
        pass


if __name__ == '__main__':
    unittest.main()
