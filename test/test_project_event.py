# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.project_event import ProjectEvent

class TestProjectEvent(unittest.TestCase):
    """ProjectEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectEvent:
        """Test ProjectEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectEvent`
        """
        model = ProjectEvent()
        if include_optional:
            return ProjectEvent(
                count = 56,
                name = ''
            )
        else:
            return ProjectEvent(
        )
        """

    def testProjectEvent(self):
        """Test ProjectEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
