# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.scanpath import Scanpath

class TestScanpath(unittest.TestCase):
    """Scanpath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Scanpath:
        """Test Scanpath
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Scanpath`
        """
        model = Scanpath()
        if include_optional:
            return Scanpath(
                end_timestamp = 1.337,
                path = [
                    None
                    ],
                start_timestamp = 1.337
            )
        else:
            return Scanpath(
        )
        """

    def testScanpath(self):
        """Test Scanpath"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
