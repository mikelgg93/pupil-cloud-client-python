# WorkspaceMembersGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[WorkspaceMember]**](WorkspaceMember.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_members_get_response import WorkspaceMembersGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMembersGetResponse from a JSON string
workspace_members_get_response_instance = WorkspaceMembersGetResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMembersGetResponse.to_json())

# convert the object into a dict
workspace_members_get_response_dict = workspace_members_get_response_instance.to_dict()
# create an instance of WorkspaceMembersGetResponse from a dict
workspace_members_get_response_from_dict = WorkspaceMembersGetResponse.from_dict(workspace_members_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


