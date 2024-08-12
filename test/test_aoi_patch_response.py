# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.aoi_patch_response import AoiPatchResponse

class TestAoiPatchResponse(unittest.TestCase):
    """AoiPatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AoiPatchResponse:
        """Test AoiPatchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AoiPatchResponse`
        """
        model = AoiPatchResponse()
        if include_optional:
            return AoiPatchResponse(
                code = 200.0,
                result = openapi_client.models.aois_response.AoisResponse(
                    bounding_box = '', 
                    centroid_xy = '', 
                    color = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by_user_id = '00000000-0000-0000-0000-000000000000', 
                    description = '', 
                    enrichment_id = '00000000-0000-0000-0000-000000000000', 
                    id = '00000000-0000-0000-0000-000000000000', 
                    mask_image_data_url = '', 
                    name = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                status = 'success'
            )
        else:
            return AoiPatchResponse(
        )
        """

    def testAoiPatchResponse(self):
        """Test AoiPatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
