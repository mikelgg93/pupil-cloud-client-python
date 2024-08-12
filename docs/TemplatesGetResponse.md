# TemplatesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Template]**](Template.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.templates_get_response import TemplatesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesGetResponse from a JSON string
templates_get_response_instance = TemplatesGetResponse.from_json(json)
# print the JSON string representation of the object
print(TemplatesGetResponse.to_json())

# convert the object into a dict
templates_get_response_dict = templates_get_response_instance.to_dict()
# create an instance of TemplatesGetResponse from a dict
templates_get_response_from_dict = TemplatesGetResponse.from_dict(templates_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


