# WorkspacesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[WorkspaceResponse]**](WorkspaceResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspaces_get_response import WorkspacesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacesGetResponse from a JSON string
workspaces_get_response_instance = WorkspacesGetResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspacesGetResponse.to_json())

# convert the object into a dict
workspaces_get_response_dict = workspaces_get_response_instance.to_dict()
# create an instance of WorkspacesGetResponse from a dict
workspaces_get_response_from_dict = WorkspacesGetResponse.from_dict(workspaces_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


