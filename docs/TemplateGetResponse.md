# TemplateGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Template**](Template.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.template_get_response import TemplateGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateGetResponse from a JSON string
template_get_response_instance = TemplateGetResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateGetResponse.to_json())

# convert the object into a dict
template_get_response_dict = template_get_response_instance.to_dict()
# create an instance of TemplateGetResponse from a dict
template_get_response_from_dict = TemplateGetResponse.from_dict(template_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


