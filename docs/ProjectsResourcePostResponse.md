# ProjectsResourcePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Project**](Project.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.projects_resource_post_response import ProjectsResourcePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsResourcePostResponse from a JSON string
projects_resource_post_response_instance = ProjectsResourcePostResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectsResourcePostResponse.to_json())

# convert the object into a dict
projects_resource_post_response_dict = projects_resource_post_response_instance.to_dict()
# create an instance of ProjectsResourcePostResponse from a dict
projects_resource_post_response_from_dict = ProjectsResourcePostResponse.from_dict(projects_resource_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


