# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.enrichment_download_spec import EnrichmentDownloadSpec

class TestEnrichmentDownloadSpec(unittest.TestCase):
    """EnrichmentDownloadSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnrichmentDownloadSpec:
        """Test EnrichmentDownloadSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnrichmentDownloadSpec`
        """
        model = EnrichmentDownloadSpec()
        if include_optional:
            return EnrichmentDownloadSpec(
                enrichment_id = '00000000-0000-0000-0000-000000000000',
                exclude_files = [
                    ''
                    ]
            )
        else:
            return EnrichmentDownloadSpec(
                enrichment_id = '00000000-0000-0000-0000-000000000000',
        )
        """

    def testEnrichmentDownloadSpec(self):
        """Test EnrichmentDownloadSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
