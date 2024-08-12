# RecordingPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**label_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**trashed_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**wearer_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_patch_request import RecordingPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingPatchRequest from a JSON string
recording_patch_request_instance = RecordingPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RecordingPatchRequest.to_json())

# convert the object into a dict
recording_patch_request_dict = recording_patch_request_instance.to_dict()
# create an instance of RecordingPatchRequest from a dict
recording_patch_request_from_dict = RecordingPatchRequest.from_dict(recording_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


