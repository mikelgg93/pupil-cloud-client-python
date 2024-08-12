# WorkspaceInvitationsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[WorkspaceInvitation]**](WorkspaceInvitation.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_invitations_get_response import WorkspaceInvitationsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationsGetResponse from a JSON string
workspace_invitations_get_response_instance = WorkspaceInvitationsGetResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationsGetResponse.to_json())

# convert the object into a dict
workspace_invitations_get_response_dict = workspace_invitations_get_response_instance.to_dict()
# create an instance of WorkspaceInvitationsGetResponse from a dict
workspace_invitations_get_response_from_dict = WorkspaceInvitationsGetResponse.from_dict(workspace_invitations_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


