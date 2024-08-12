# WorkspaceMemberDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[WorkspaceMember]**](WorkspaceMember.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_member_delete_response import WorkspaceMemberDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberDeleteResponse from a JSON string
workspace_member_delete_response_instance = WorkspaceMemberDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberDeleteResponse.to_json())

# convert the object into a dict
workspace_member_delete_response_dict = workspace_member_delete_response_instance.to_dict()
# create an instance of WorkspaceMemberDeleteResponse from a dict
workspace_member_delete_response_from_dict = WorkspaceMemberDeleteResponse.from_dict(workspace_member_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


