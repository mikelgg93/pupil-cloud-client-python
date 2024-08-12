# ProjectResourceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Project**](Project.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_resource_get_response import ProjectResourceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResourceGetResponse from a JSON string
project_resource_get_response_instance = ProjectResourceGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectResourceGetResponse.to_json())

# convert the object into a dict
project_resource_get_response_dict = project_resource_get_response_instance.to_dict()
# create an instance of ProjectResourceGetResponse from a dict
project_resource_get_response_from_dict = ProjectResourceGetResponse.from_dict(project_resource_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


