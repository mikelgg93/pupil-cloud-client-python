# LabelPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aoi_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**recording_ids** | **List[str]** |  | [optional] 
**template_ids** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.label_patch_request import LabelPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPatchRequest from a JSON string
label_patch_request_instance = LabelPatchRequest.from_json(json)
# print the JSON string representation of the object
print(LabelPatchRequest.to_json())

# convert the object into a dict
label_patch_request_dict = label_patch_request_instance.to_dict()
# create an instance of LabelPatchRequest from a dict
label_patch_request_from_dict = LabelPatchRequest.from_dict(label_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


