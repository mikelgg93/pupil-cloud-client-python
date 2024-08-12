# ProjectUniqueEventsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[ProjectEvent]**](ProjectEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_unique_events_get_response import ProjectUniqueEventsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUniqueEventsGetResponse from a JSON string
project_unique_events_get_response_instance = ProjectUniqueEventsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectUniqueEventsGetResponse.to_json())

# convert the object into a dict
project_unique_events_get_response_dict = project_unique_events_get_response_instance.to_dict()
# create an instance of ProjectUniqueEventsGetResponse from a dict
project_unique_events_get_response_from_dict = ProjectUniqueEventsGetResponse.from_dict(project_unique_events_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


