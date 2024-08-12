# RecordingPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**RecordingWithFilesResponse**](RecordingWithFilesResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_patch_response import RecordingPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingPatchResponse from a JSON string
recording_patch_response_instance = RecordingPatchResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingPatchResponse.to_json())

# convert the object into a dict
recording_patch_response_dict = recording_patch_response_instance.to_dict()
# create an instance of RecordingPatchResponse from a dict
recording_patch_response_from_dict = RecordingPatchResponse.from_dict(recording_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


