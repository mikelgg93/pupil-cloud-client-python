# ProjectEventsResourceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[ProjectRecordingEvent]**](ProjectRecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_events_resource_get_response import ProjectEventsResourceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEventsResourceGetResponse from a JSON string
project_events_resource_get_response_instance = ProjectEventsResourceGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectEventsResourceGetResponse.to_json())

# convert the object into a dict
project_events_resource_get_response_dict = project_events_resource_get_response_instance.to_dict()
# create an instance of ProjectEventsResourceGetResponse from a dict
project_events_resource_get_response_from_dict = ProjectEventsResourceGetResponse.from_dict(project_events_resource_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


