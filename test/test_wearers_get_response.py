# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.wearers_get_response import WearersGetResponse

class TestWearersGetResponse(unittest.TestCase):
    """WearersGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WearersGetResponse:
        """Test WearersGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WearersGetResponse`
        """
        model = WearersGetResponse()
        if include_optional:
            return WearersGetResponse(
                code = 200.0,
                result = [
                    openapi_client.models.wearer.Wearer(
                        archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        archived_by_user_id = '00000000-0000-0000-0000-000000000000', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created_by_user_id = '00000000-0000-0000-0000-000000000000', 
                        id = '00000000-0000-0000-0000-000000000000', 
                        ied = 1.337, 
                        name = '0', 
                        offset_correction = openapi_client.models.offset_correction.OffsetCorrection(
                            x = 1.337, 
                            y = 1.337, ), 
                        training_updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        workspace_id = '00000000-0000-0000-0000-000000000000', )
                    ],
                status = 'success'
            )
        else:
            return WearersGetResponse(
        )
        """

    def testWearersGetResponse(self):
        """Test WearersGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
