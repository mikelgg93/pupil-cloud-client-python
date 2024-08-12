# WorkspaceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha_features** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**default_template_id** | **str** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] 
**deleted_by_user_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**picture_url** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] [readonly] 
**raw_file_downloads** | **bool** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 
**world_video_mode** | **str** | world video mode | [optional] 

## Example

```python
from pupilcloud.models.workspace_response import WorkspaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceResponse from a JSON string
workspace_response_instance = WorkspaceResponse.from_json(json)
# print the JSON string representation of the object
print(WorkspaceResponse.to_json())

# convert the object into a dict
workspace_response_dict = workspace_response_instance.to_dict()
# create an instance of WorkspaceResponse from a dict
workspace_response_from_dict = WorkspaceResponse.from_dict(workspace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


