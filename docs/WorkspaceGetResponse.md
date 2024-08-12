# WorkspaceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorkspaceResponse**](WorkspaceResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.workspace_get_response import WorkspaceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceGetResponse from a JSON string
workspace_get_response_instance = WorkspaceGetResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceGetResponse.to_json())

# convert the object into a dict
workspace_get_response_dict = workspace_get_response_instance.to_dict()
# create an instance of WorkspaceGetResponse from a dict
workspace_get_response_from_dict = WorkspaceGetResponse.from_dict(workspace_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


