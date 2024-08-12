# ProjectRecordingEventsResourcePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**ProjectRecordingEvent**](ProjectRecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_recording_events_resource_post_response import ProjectRecordingEventsResourcePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRecordingEventsResourcePostResponse from a JSON string
project_recording_events_resource_post_response_instance = ProjectRecordingEventsResourcePostResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectRecordingEventsResourcePostResponse.to_json())

# convert the object into a dict
project_recording_events_resource_post_response_dict = project_recording_events_resource_post_response_instance.to_dict()
# create an instance of ProjectRecordingEventsResourcePostResponse from a dict
project_recording_events_resource_post_response_from_dict = ProjectRecordingEventsResourcePostResponse.from_dict(project_recording_events_resource_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


