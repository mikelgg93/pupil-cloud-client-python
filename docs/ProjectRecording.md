# ProjectRecording


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ProjectEvent]**](ProjectEvent.md) |  | [optional] 
**project_id** | **str** |  | [optional] 
**recording_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_recording import ProjectRecording

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRecording from a JSON string
project_recording_instance = ProjectRecording.from_json(json)
# print the JSON string representation of the object
print(ProjectRecording.to_json())

# convert the object into a dict
project_recording_dict = project_recording_instance.to_dict()
# create an instance of ProjectRecording from a dict
project_recording_from_dict = ProjectRecording.from_dict(project_recording_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


