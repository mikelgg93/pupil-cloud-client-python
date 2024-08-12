# AcceptInvitationResourcePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceMember**](WorkspaceMember.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.accept_invitation_resource_post_response import AcceptInvitationResourcePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptInvitationResourcePostResponse from a JSON string
accept_invitation_resource_post_response_instance = AcceptInvitationResourcePostResponse.from_json(json)
# print the JSON string representation of the object
print(AcceptInvitationResourcePostResponse.to_json())

# convert the object into a dict
accept_invitation_resource_post_response_dict = accept_invitation_resource_post_response_instance.to_dict()
# create an instance of AcceptInvitationResourcePostResponse from a dict
accept_invitation_resource_post_response_from_dict = AcceptInvitationResourcePostResponse.from_dict(accept_invitation_resource_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


