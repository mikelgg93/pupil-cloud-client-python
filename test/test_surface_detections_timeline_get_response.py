# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.surface_detections_timeline_get_response import SurfaceDetectionsTimelineGetResponse

class TestSurfaceDetectionsTimelineGetResponse(unittest.TestCase):
    """SurfaceDetectionsTimelineGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SurfaceDetectionsTimelineGetResponse:
        """Test SurfaceDetectionsTimelineGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SurfaceDetectionsTimelineGetResponse`
        """
        model = SurfaceDetectionsTimelineGetResponse()
        if include_optional:
            return SurfaceDetectionsTimelineGetResponse(
                code = 200.0,
                result = [
                    openapi_client.models.surface_timeline.SurfaceTimeline(
                        aoi_detected = 1.337, 
                        avg_gaze_on_aoi = 1.337, 
                        end_timestamp = 1.337, 
                        gaze_on_aoi = 1.337, 
                        start_timestamp = 1.337, 
                        sum_gaze_on_aoi = 56, 
                        total_frames = 56, )
                    ],
                status = 'success'
            )
        else:
            return SurfaceDetectionsTimelineGetResponse(
        )
        """

    def testSurfaceDetectionsTimelineGetResponse(self):
        """Test SurfaceDetectionsTimelineGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
