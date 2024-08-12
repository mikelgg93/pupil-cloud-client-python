# TemplatePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Template**](Template.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.template_patch_response import TemplatePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatePatchResponse from a JSON string
template_patch_response_instance = TemplatePatchResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatePatchResponse.to_json())

# convert the object into a dict
template_patch_response_dict = template_patch_response_instance.to_dict()
# create an instance of TemplatePatchResponse from a dict
template_patch_response_from_dict = TemplatePatchResponse.from_dict(template_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


