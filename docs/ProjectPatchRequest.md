# ProjectPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**filter_ids** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**recording_ids** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.project_patch_request import ProjectPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectPatchRequest from a JSON string
project_patch_request_instance = ProjectPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectPatchRequest.to_json())

# convert the object into a dict
project_patch_request_dict = project_patch_request_instance.to_dict()
# create an instance of ProjectPatchRequest from a dict
project_patch_request_from_dict = ProjectPatchRequest.from_dict(project_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


