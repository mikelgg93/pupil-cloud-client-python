# TemplatePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Template**](Template.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.template_post_response import TemplatePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePostResponse from a JSON string
template_post_response_instance = TemplatePostResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatePostResponse.to_json())

# convert the object into a dict
template_post_response_dict = template_post_response_instance.to_dict()
# create an instance of TemplatePostResponse from a dict
template_post_response_from_dict = TemplatePostResponse.from_dict(template_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


