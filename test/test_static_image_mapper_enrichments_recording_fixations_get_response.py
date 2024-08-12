# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.static_image_mapper_enrichments_recording_fixations_get_response import StaticImageMapperEnrichmentsRecordingFixationsGetResponse

class TestStaticImageMapperEnrichmentsRecordingFixationsGetResponse(unittest.TestCase):
    """StaticImageMapperEnrichmentsRecordingFixationsGetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StaticImageMapperEnrichmentsRecordingFixationsGetResponse:
        """Test StaticImageMapperEnrichmentsRecordingFixationsGetResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StaticImageMapperEnrichmentsRecordingFixationsGetResponse`
        """
        model = StaticImageMapperEnrichmentsRecordingFixationsGetResponse()
        if include_optional:
            return StaticImageMapperEnrichmentsRecordingFixationsGetResponse(
                code = 200.0,
                result = openapi_client.models.recording_fixations.RecordingFixations(
                    checked_fixations = 56, 
                    total_fixations = 56, ),
                status = 'success'
            )
        else:
            return StaticImageMapperEnrichmentsRecordingFixationsGetResponse(
        )
        """

    def testStaticImageMapperEnrichmentsRecordingFixationsGetResponse(self):
        """Test StaticImageMapperEnrichmentsRecordingFixationsGetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
