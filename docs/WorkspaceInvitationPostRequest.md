# WorkspaceInvitationPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from pupilcloud.models.workspace_invitation_post_request import WorkspaceInvitationPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceInvitationPostRequest from a JSON string
workspace_invitation_post_request_instance = WorkspaceInvitationPostRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceInvitationPostRequest.to_json())

# convert the object into a dict
workspace_invitation_post_request_dict = workspace_invitation_post_request_instance.to_dict()
# create an instance of WorkspaceInvitationPostRequest from a dict
workspace_invitation_post_request_from_dict = WorkspaceInvitationPostRequest.from_dict(workspace_invitation_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


