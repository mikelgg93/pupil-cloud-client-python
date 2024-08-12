# WorkspaceInvitationCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceInvitation**](WorkspaceInvitation.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_invitation_create_response import WorkspaceInvitationCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationCreateResponse from a JSON string
workspace_invitation_create_response_instance = WorkspaceInvitationCreateResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationCreateResponse.to_json())

# convert the object into a dict
workspace_invitation_create_response_dict = workspace_invitation_create_response_instance.to_dict()
# create an instance of WorkspaceInvitationCreateResponse from a dict
workspace_invitation_create_response_from_dict = WorkspaceInvitationCreateResponse.from_dict(workspace_invitation_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


