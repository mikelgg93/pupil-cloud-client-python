# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.labels_api import LabelsApi


class TestLabelsApi(unittest.TestCase):
    """LabelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LabelsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_label(self) -> None:
        """Test case for delete_label

        Delete a label
        """
        pass

    def test_delete_labels(self) -> None:
        """Test case for delete_labels

        Delete multiple labels
        """
        pass

    def test_get_label(self) -> None:
        """Test case for get_label

        Returns a label with {label_id}
        """
        pass

    def test_get_labels(self) -> None:
        """Test case for get_labels

        List all labels
        """
        pass

    def test_patch_label(self) -> None:
        """Test case for patch_label

        Update a label
        """
        pass

    def test_post_label(self) -> None:
        """Test case for post_label

        Create a new label
        """
        pass

    def test_post_label_0(self) -> None:
        """Test case for post_label_0

        Create a new label
        """
        pass


if __name__ == '__main__':
    unittest.main()
