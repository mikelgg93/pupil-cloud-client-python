# Recording


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
from pupilcloud.models.recording import Recording

# TODO update the JSON string below
json = "{}"
# create an instance of Recording from a JSON string
recording_instance = Recording.from_json(json)
# print the JSON string representation of the object
print(Recording.to_json())

# convert the object into a dict
recording_dict = recording_instance.to_dict()
# create an instance of Recording from a dict
recording_from_dict = Recording.from_dict(recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


