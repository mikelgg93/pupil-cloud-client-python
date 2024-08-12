# ProjectsResourceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Project]**](Project.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.projects_resource_get_response import ProjectsResourceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsResourceGetResponse from a JSON string
projects_resource_get_response_instance = ProjectsResourceGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectsResourceGetResponse.to_json())

# convert the object into a dict
projects_resource_get_response_dict = projects_resource_get_response_instance.to_dict()
# create an instance of ProjectsResourceGetResponse from a dict
projects_resource_get_response_from_dict = ProjectsResourceGetResponse.from_dict(projects_resource_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


