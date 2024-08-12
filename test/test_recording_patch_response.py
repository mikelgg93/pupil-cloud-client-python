# coding: utf-8

"""
    Pupil Cloud

    Pupil Cloud API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.recording_patch_response import RecordingPatchResponse

class TestRecordingPatchResponse(unittest.TestCase):
    """RecordingPatchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecordingPatchResponse:
        """Test RecordingPatchResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecordingPatchResponse`
        """
        model = RecordingPatchResponse()
        if include_optional:
            return RecordingPatchResponse(
                code = 200.0,
                result = openapi_client.models.recording_with_files_response.RecordingWithFilesResponse(
                    android_gaze_offset = openapi_client.models.offset_correction.OffsetCorrection(
                        x = 1.337, 
                        y = 1.337, ), 
                    app_version = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by_user_id = '00000000-0000-0000-0000-000000000000', 
                    device_model = '', 
                    device_name = '', 
                    duration_ns = 56, 
                    family = 'i', 
                    file_ids = [
                        '00000000-0000-0000-0000-000000000000'
                        ], 
                    files = [
                        openapi_client.models.recording_file.RecordingFile(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '00000000-0000-0000-0000-000000000000', 
                            mimetype = '', 
                            name = '', 
                            size_bytes = 56, 
                            started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            uploaded_bytes = 56, 
                            workspace_id = '00000000-0000-0000-0000-000000000000', )
                        ], 
                    gaze_offset = openapi_client.models.offset_correction.OffsetCorrection(
                        x = 1.337, 
                        y = 1.337, ), 
                    gaze_offset_x = 1.337, 
                    gaze_offset_y = 1.337, 
                    gazepipeline_status = 'queued', 
                    glasses_id = '', 
                    has_scanpath = True, 
                    id = '00000000-0000-0000-0000-000000000000', 
                    is_blurred = True, 
                    is_processed = True, 
                    is_silent = True, 
                    is_uploaded = True, 
                    is_viewable = True, 
                    label_ids = [
                        '00000000-0000-0000-0000-000000000000'
                        ], 
                    name = '', 
                    preprocessing_error_message = '', 
                    recorded_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    recording_hash = '', 
                    scene_camera_id = '', 
                    sensors = [
                        ''
                        ], 
                    size = 56, 
                    template_data = {
                        'key' : [
                            ''
                            ]
                        }, 
                    template_id = '00000000-0000-0000-0000-000000000000', 
                    thumbnail_url = '', 
                    transcoded_url = '', 
                    transcoding_status = 'queued', 
                    trashed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    trashed_by_user_id = '00000000-0000-0000-0000-000000000000', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    uploaded_bytes = 56, 
                    wearer_id = '00000000-0000-0000-0000-000000000000', 
                    workspace_id = '00000000-0000-0000-0000-000000000000', ),
                status = 'success'
            )
        else:
            return RecordingPatchResponse(
        )
        """

    def testRecordingPatchResponse(self):
        """Test RecordingPatchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
