# ProjectRecordingEventResourcePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**ProjectRecordingEvent**](ProjectRecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_recording_event_resource_patch_response import ProjectRecordingEventResourcePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRecordingEventResourcePatchResponse from a JSON string
project_recording_event_resource_patch_response_instance = ProjectRecordingEventResourcePatchResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectRecordingEventResourcePatchResponse.to_json())

# convert the object into a dict
project_recording_event_resource_patch_response_dict = project_recording_event_resource_patch_response_instance.to_dict()
# create an instance of ProjectRecordingEventResourcePatchResponse from a dict
project_recording_event_resource_patch_response_from_dict = ProjectRecordingEventResourcePatchResponse.from_dict(project_recording_event_resource_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


