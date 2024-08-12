# WorkspacePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha_features** | **bool** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] 
**default_template_id** | **str** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] 
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
from pupilcloud.models.workspace_post_request import WorkspacePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspacePostRequest from a JSON string
workspace_post_request_instance = WorkspacePostRequest.from_json(json)
# print the JSON string representation of the object
print(WorkspacePostRequest.to_json())

# convert the object into a dict
workspace_post_request_dict = workspace_post_request_instance.to_dict()
# create an instance of WorkspacePostRequest from a dict
workspace_post_request_from_dict = WorkspacePostRequest.from_dict(workspace_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


