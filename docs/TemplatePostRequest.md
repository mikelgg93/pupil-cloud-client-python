# TemplatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**items** | [**List[TemplateItem]**](TemplateItem.md) |  | [optional] 
**name** | **str** |  | 
**published_at** | **datetime** |  | [optional] 
**recording_name_format** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.template_post_request import TemplatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePostRequest from a JSON string
template_post_request_instance = TemplatePostRequest.from_json(json)
# print the JSON string representation of the object
print(TemplatePostRequest.to_json())

# convert the object into a dict
template_post_request_dict = template_post_request_instance.to_dict()
# create an instance of TemplatePostRequest from a dict
template_post_request_from_dict = TemplatePostRequest.from_dict(template_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


