# TemplatesDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_ids** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.templates_delete_request import TemplatesDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesDeleteRequest from a JSON string
templates_delete_request_instance = TemplatesDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(TemplatesDeleteRequest.to_json())

# convert the object into a dict
templates_delete_request_dict = templates_delete_request_instance.to_dict()
# create an instance of TemplatesDeleteRequest from a dict
templates_delete_request_from_dict = TemplatesDeleteRequest.from_dict(templates_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


