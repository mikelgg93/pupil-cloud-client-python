# ProjectEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_event import ProjectEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEvent from a JSON string
project_event_instance = ProjectEvent.from_json(json)
# print the JSON string representation of the object
print(ProjectEvent.to_json())

# convert the object into a dict
project_event_dict = project_event_instance.to_dict()
# create an instance of ProjectEvent from a dict
project_event_from_dict = ProjectEvent.from_dict(project_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


