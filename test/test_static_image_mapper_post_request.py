# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.static_image_mapper_post_request import StaticImageMapperPostRequest

class TestStaticImageMapperPostRequest(unittest.TestCase):
    """StaticImageMapperPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaticImageMapperPostRequest:
        """Test StaticImageMapperPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaticImageMapperPostRequest`
        """
        model = StaticImageMapperPostRequest()
        if include_optional:
            return StaticImageMapperPostRequest(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                from_event_name = '',
                name = '',
                static_image_id = '00000000-0000-0000-0000-000000000000',
                to_event_name = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return StaticImageMapperPostRequest(
                from_event_name = '',
                name = '',
                to_event_name = '',
        )
        """

    def testStaticImageMapperPostRequest(self):
        """Test StaticImageMapperPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
