# WorkspaceMemberPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 
**user_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_member_post_request import WorkspaceMemberPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceMemberPostRequest from a JSON string
workspace_member_post_request_instance = WorkspaceMemberPostRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspaceMemberPostRequest.to_json())

# convert the object into a dict
workspace_member_post_request_dict = workspace_member_post_request_instance.to_dict()
# create an instance of WorkspaceMemberPostRequest from a dict
workspace_member_post_request_from_dict = WorkspaceMemberPostRequest.from_dict(workspace_member_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


