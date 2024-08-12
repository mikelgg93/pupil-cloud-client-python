# ProjectRecordingEventPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**offset_s** | **float** | time offset within recording (seconds) | 
**origin** | **str** | origin of the event (recording events can not be created/deleted, only suppressed) | 
**project_id** | **str** |  | [optional] 
**recording_id** | **str** |  | [optional] 
**suppressed** | **bool** | event should be ignored when processing | [optional] [default to False]
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.project_recording_event_patch_request import ProjectRecordingEventPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRecordingEventPatchRequest from a JSON string
project_recording_event_patch_request_instance = ProjectRecordingEventPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectRecordingEventPatchRequest.to_json())

# convert the object into a dict
project_recording_event_patch_request_dict = project_recording_event_patch_request_instance.to_dict()
# create an instance of ProjectRecordingEventPatchRequest from a dict
project_recording_event_patch_request_from_dict = ProjectRecordingEventPatchRequest.from_dict(project_recording_event_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


