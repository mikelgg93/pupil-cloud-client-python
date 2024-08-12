# WorkspaceInvitationsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[WorkspaceInvitation]**](WorkspaceInvitation.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_invitations_list_response import WorkspaceInvitationsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationsListResponse from a JSON string
workspace_invitations_list_response_instance = WorkspaceInvitationsListResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationsListResponse.to_json())

# convert the object into a dict
workspace_invitations_list_response_dict = workspace_invitations_list_response_instance.to_dict()
# create an instance of WorkspaceInvitationsListResponse from a dict
workspace_invitations_list_response_from_dict = WorkspaceInvitationsListResponse.from_dict(workspace_invitations_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


