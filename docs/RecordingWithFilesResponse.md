# RecordingWithFilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_gaze_offset** | [**OffsetCorrection**](OffsetCorrection.md) |  | [optional] 
**app_version** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**device_model** | **str** |  | [optional] 
**device_name** | **str** |  | [optional] 
**duration_ns** | **int** |  | [optional] 
**family** | **str** |  | [optional] 
**file_ids** | **List[str]** |  | [optional] 
**files** | [**List[RecordingFile]**](RecordingFile.md) |  | [optional] 
**gaze_offset** | [**OffsetCorrection**](OffsetCorrection.md) |  | [optional] 
**gaze_offset_x** | **float** |  | [optional] 
**gaze_offset_y** | **float** |  | [optional] 
**gazepipeline_status** | **str** |  | [optional] 
**glasses_id** | **str** |  | [optional] 
**has_scanpath** | **bool** |  | [optional] [default to False]
**id** | **str** |  | [optional] 
**is_blurred** | **bool** |  | [optional] [default to False]
**is_processed** | **bool** |  | [optional] 
**is_silent** | **bool** |  | [optional] 
**is_uploaded** | **bool** |  | [optional] 
**is_viewable** | **bool** |  | [optional] 
**label_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**preprocessing_error_message** | **str** |  | [optional] 
**recorded_at** | **datetime** |  | [optional] 
**recording_hash** | **str** |  | [optional] 
**scene_camera_id** | **str** |  | [optional] 
**sensors** | **List[str]** |  | [optional] 
**size** | **int** |  | [optional] 
**template_data** | **Dict[str, List[str]]** |  | [optional] 
**template_id** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**transcoded_url** | **str** |  | [optional] 
**transcoding_status** | **str** |  | [optional] 
**trashed_at** | **datetime** |  | [optional] 
**trashed_by_user_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**uploaded_bytes** | **int** |  | [optional] 
**wearer_id** | **str** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_with_files_response import RecordingWithFilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingWithFilesResponse from a JSON string
recording_with_files_response_instance = RecordingWithFilesResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingWithFilesResponse.to_json())

# convert the object into a dict
recording_with_files_response_dict = recording_with_files_response_instance.to_dict()
# create an instance of RecordingWithFilesResponse from a dict
recording_with_files_response_from_dict = RecordingWithFilesResponse.from_dict(recording_with_files_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


