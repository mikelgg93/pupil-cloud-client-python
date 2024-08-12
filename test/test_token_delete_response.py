# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.token_delete_response import TokenDeleteResponse

class TestTokenDeleteResponse(unittest.TestCase):
    """TokenDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TokenDeleteResponse:
        """Test TokenDeleteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenDeleteResponse`
        """
        model = TokenDeleteResponse()
        if include_optional:
            return TokenDeleteResponse(
                code = 200.0,
                result = openapi_client.models.token.Token(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    id = '', 
                    last_used_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    token = '', ),
                status = 'success'
            )
        else:
            return TokenDeleteResponse(
        )
        """

    def testTokenDeleteResponse(self):
        """Test TokenDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
