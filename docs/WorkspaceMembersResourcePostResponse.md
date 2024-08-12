# WorkspaceMembersResourcePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceMember**](WorkspaceMember.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_members_resource_post_response import WorkspaceMembersResourcePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembersResourcePostResponse from a JSON string
workspace_members_resource_post_response_instance = WorkspaceMembersResourcePostResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMembersResourcePostResponse.to_json())

# convert the object into a dict
workspace_members_resource_post_response_dict = workspace_members_resource_post_response_instance.to_dict()
# create an instance of WorkspaceMembersResourcePostResponse from a dict
workspace_members_resource_post_response_from_dict = WorkspaceMembersResourcePostResponse.from_dict(workspace_members_resource_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


