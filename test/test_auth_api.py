# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.auth_api import AuthApi


class TestAuthApi(unittest.TestCase):
    """AuthApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthApi()

    def tearDown(self) -> None:
        pass

    def test_delete_token(self) -> None:
        """Test case for delete_token

        Delete an access token
        """
        pass

    def test_delete_workspace_invitation(self) -> None:
        """Test case for delete_workspace_invitation

        Delete a workspace invitation
        """
        pass

    def test_get_canny_sso_token(self) -> None:
        """Test case for get_canny_sso_token

        Returns the canny
        """
        pass

    def test_get_profile(self) -> None:
        """Test case for get_profile

        Returns the current logged in user based on auth token
        """
        pass

    def test_get_token(self) -> None:
        """Test case for get_token

        Get an access token
        """
        pass

    def test_get_tokens(self) -> None:
        """Test case for get_tokens

        Get all access tokens
        """
        pass

    def test_get_workspace_invitation(self) -> None:
        """Test case for get_workspace_invitation

        get workspace inviation for token
        """
        pass

    def test_get_workspace_invitations(self) -> None:
        """Test case for get_workspace_invitations

        List all workspace inviations for current user
        """
        pass

    def test_patch_profile(self) -> None:
        """Test case for patch_profile

        Update user profile
        """
        pass

    def test_post_accept_invitation_resource(self) -> None:
        """Test case for post_accept_invitation_resource

        Create workspace member based on invite token
        """
        pass

    def test_post_login(self) -> None:
        """Test case for post_login

        Login the user and return a new session cookie
        """
        pass

    def test_post_logout(self) -> None:
        """Test case for post_logout

        Logout the current user
        """
        pass

    def test_post_token(self) -> None:
        """Test case for post_token

        Creates a new access token
        """
        pass

    def test_post_unregister(self) -> None:
        """Test case for post_unregister

        Unregisters the currently logged in user
        """
        pass


if __name__ == '__main__':
    unittest.main()
