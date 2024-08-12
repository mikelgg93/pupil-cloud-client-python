# WorkspaceMemberPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceMember**](WorkspaceMember.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_member_patch_response import WorkspaceMemberPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberPatchResponse from a JSON string
workspace_member_patch_response_instance = WorkspaceMemberPatchResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberPatchResponse.to_json())

# convert the object into a dict
workspace_member_patch_response_dict = workspace_member_patch_response_instance.to_dict()
# create an instance of WorkspaceMemberPatchResponse from a dict
workspace_member_patch_response_from_dict = WorkspaceMemberPatchResponse.from_dict(workspace_member_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


