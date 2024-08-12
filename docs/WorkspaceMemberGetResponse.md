# WorkspaceMemberGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceMember**](WorkspaceMember.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_member_get_response import WorkspaceMemberGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberGetResponse from a JSON string
workspace_member_get_response_instance = WorkspaceMemberGetResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberGetResponse.to_json())

# convert the object into a dict
workspace_member_get_response_dict = workspace_member_get_response_instance.to_dict()
# create an instance of WorkspaceMemberGetResponse from a dict
workspace_member_get_response_from_dict = WorkspaceMemberGetResponse.from_dict(workspace_member_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


