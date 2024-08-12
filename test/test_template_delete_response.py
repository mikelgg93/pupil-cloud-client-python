# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.template_delete_response import TemplateDeleteResponse

class TestTemplateDeleteResponse(unittest.TestCase):
    """TemplateDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplateDeleteResponse:
        """Test TemplateDeleteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplateDeleteResponse`
        """
        model = TemplateDeleteResponse()
        if include_optional:
            return TemplateDeleteResponse(
                code = 200.0,
                result = openapi_client.models.template.Template(
                    archived_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    archived_by_user_id = '00000000-0000-0000-0000-000000000000', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by_user_id = '00000000-0000-0000-0000-000000000000', 
                    id = '00000000-0000-0000-0000-000000000000', 
                    is_default_template = True, 
                    items = [
                        openapi_client.models.template_item.TemplateItem(
                            choices = [
                                ''
                                ], 
                            help_text = '', 
                            id = '00000000-0000-0000-0000-000000000000', 
                            input_type = 'any', 
                            required = True, 
                            title = '', 
                            widget_type = 'TEXT', )
                        ], 
                    label_ids = [
                        '00000000-0000-0000-0000-000000000000'
                        ], 
                    name = '', 
                    published_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    recording_ids = [
                        '00000000-0000-0000-0000-000000000000'
                        ], 
                    recording_name_format = [
                        ''
                        ], 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                status = 'success'
            )
        else:
            return TemplateDeleteResponse(
        )
        """

    def testTemplateDeleteResponse(self):
        """Test TemplateDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
