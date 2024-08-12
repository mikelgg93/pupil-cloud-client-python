# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.render_patch_response import RenderPatchResponse

class TestRenderPatchResponse(unittest.TestCase):
    """RenderPatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenderPatchResponse:
        """Test RenderPatchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenderPatchResponse`
        """
        model = RenderPatchResponse()
        if include_optional:
            return RenderPatchResponse(
                code = 200.0,
                result = openapi_client.models.world_render.WorldRender(
                    audio = True, 
                    gaze_circle = openapi_client.models.gaze_circle.GazeCircle(
                        color = openapi_client.models.color.Color(
                            alpha = 0, 
                            blue = 0, 
                            green = 0, 
                            red = 0, ), 
                        radius = 56, 
                        stroke_width = 56, ), 
                    id = '00000000-0000-0000-0000-000000000000', 
                    undistort_frames = True, 
                    with_gaze = True, 
                    with_scanpath = True, 
                    with_timestamps = True, ),
                status = 'success'
            )
        else:
            return RenderPatchResponse(
        )
        """

    def testRenderPatchResponse(self):
        """Test RenderPatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
