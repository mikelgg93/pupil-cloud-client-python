# ProjectRecordingsResourceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[ProjectRecording]**](ProjectRecording.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_recordings_resource_get_response import ProjectRecordingsResourceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRecordingsResourceGetResponse from a JSON string
project_recordings_resource_get_response_instance = ProjectRecordingsResourceGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectRecordingsResourceGetResponse.to_json())

# convert the object into a dict
project_recordings_resource_get_response_dict = project_recordings_resource_get_response_instance.to_dict()
# create an instance of ProjectRecordingsResourceGetResponse from a dict
project_recordings_resource_get_response_from_dict = ProjectRecordingsResourceGetResponse.from_dict(project_recordings_resource_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


