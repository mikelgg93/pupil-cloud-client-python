# ProjectsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.projects_delete_request import ProjectsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsDeleteRequest from a JSON string
projects_delete_request_instance = ProjectsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsDeleteRequest.to_json())

# convert the object into a dict
projects_delete_request_dict = projects_delete_request_instance.to_dict()
# create an instance of ProjectsDeleteRequest from a dict
projects_delete_request_from_dict = ProjectsDeleteRequest.from_dict(projects_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


