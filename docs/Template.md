# Template


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **datetime** |  | [optional] 
**archived_by_user_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_default_template** | **bool** |  | [optional] [readonly] 
**items** | [**List[TemplateItem]**](TemplateItem.md) |  | [optional] 
**label_ids** | **List[str]** |  | [optional] [readonly] 
**name** | **str** |  | 
**published_at** | **datetime** |  | [optional] 
**recording_ids** | **List[str]** |  | [optional] [readonly] 
**recording_name_format** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.template import Template

# TODO update the JSON string below
json = "{}"
# create an instance of Template from a JSON string
template_instance = Template.from_json(json)
# print the JSON string representation of the object
print(Template.to_json())

# convert the object into a dict
template_dict = template_instance.to_dict()
# create an instance of Template from a dict
template_from_dict = Template.from_dict(template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


