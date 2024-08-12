# WorkspacePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceResponse**](WorkspaceResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_post_response import WorkspacePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePostResponse from a JSON string
workspace_post_response_instance = WorkspacePostResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspacePostResponse.to_json())

# convert the object into a dict
workspace_post_response_dict = workspace_post_response_instance.to_dict()
# create an instance of WorkspacePostResponse from a dict
workspace_post_response_from_dict = WorkspacePostResponse.from_dict(workspace_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


