# TemplateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | **List[str]** |  | [optional] 
**help_text** | **str** | short optional help text for the item | [optional] 
**id** | **str** |  | [optional] 
**input_type** | **str** | the basic type of the value for this item&#39;s input | [optional] [default to 'any']
**required** | **bool** | if value is required | [optional] 
**title** | **str** | title of item | [optional] 
**widget_type** | **str** | widget to use for this item | 

## Example

```python
from pupilcloud.models.template_item import TemplateItem

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateItem from a JSON string
template_item_instance = TemplateItem.from_json(json)
# print the JSON string representation of the object
print(TemplateItem.to_json())

# convert the object into a dict
template_item_dict = template_item_instance.to_dict()
# create an instance of TemplateItem from a dict
template_item_from_dict = TemplateItem.from_dict(template_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


