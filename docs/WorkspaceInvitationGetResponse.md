# WorkspaceInvitationGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceInvitation**](WorkspaceInvitation.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_invitation_get_response import WorkspaceInvitationGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationGetResponse from a JSON string
workspace_invitation_get_response_instance = WorkspaceInvitationGetResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationGetResponse.to_json())

# convert the object into a dict
workspace_invitation_get_response_dict = workspace_invitation_get_response_instance.to_dict()
# create an instance of WorkspaceInvitationGetResponse from a dict
workspace_invitation_get_response_from_dict = WorkspaceInvitationGetResponse.from_dict(workspace_invitation_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


