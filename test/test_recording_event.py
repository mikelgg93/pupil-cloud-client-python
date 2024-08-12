# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.recording_event import RecordingEvent

class TestRecordingEvent(unittest.TestCase):
    """RecordingEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordingEvent:
        """Test RecordingEvent
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordingEvent`
        """
        model = RecordingEvent()
        if include_optional:
            return RecordingEvent(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_by_user_id = '00000000-0000-0000-0000-000000000000',
                epoch_ns = 56,
                id = '00000000-0000-0000-0000-000000000000',
                name = '',
                offset_s = 1.337,
                origin = 'recording',
                recording_id = '00000000-0000-0000-0000-000000000000',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return RecordingEvent(
                origin = 'recording',
        )
        """

    def testRecordingEvent(self):
        """Test RecordingEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
