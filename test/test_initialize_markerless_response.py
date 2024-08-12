# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.initialize_markerless_response import InitializeMarkerlessResponse

class TestInitializeMarkerlessResponse(unittest.TestCase):
    """InitializeMarkerlessResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InitializeMarkerlessResponse:
        """Test InitializeMarkerlessResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InitializeMarkerlessResponse`
        """
        model = InitializeMarkerlessResponse()
        if include_optional:
            return InitializeMarkerlessResponse(
                code = 200.0,
                result = openapi_client.models.markerless.Markerless(
                    id = '00000000-0000-0000-0000-000000000000', 
                    reference_image_id = '00000000-0000-0000-0000-000000000000', 
                    reference_image_thumbnail_url = '', 
                    scanning_recording_id = '00000000-0000-0000-0000-000000000000', ),
                status = 'success'
            )
        else:
            return InitializeMarkerlessResponse(
        )
        """

    def testInitializeMarkerlessResponse(self):
        """Test InitializeMarkerlessResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
