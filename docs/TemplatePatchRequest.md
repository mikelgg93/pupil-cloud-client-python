# TemplatePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | [**List[TemplateItem]**](TemplateItem.md) |  | [optional] 
**label_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | 
**published_at** | **datetime** |  | [optional] 
**recording_name_format** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.template_patch_request import TemplatePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePatchRequest from a JSON string
template_patch_request_instance = TemplatePatchRequest.from_json(json)
# print the JSON string representation of the object
print(TemplatePatchRequest.to_json())

# convert the object into a dict
template_patch_request_dict = template_patch_request_instance.to_dict()
# create an instance of TemplatePatchRequest from a dict
template_patch_request_from_dict = TemplatePatchRequest.from_dict(template_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


