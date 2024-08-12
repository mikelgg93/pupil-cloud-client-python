# FiltersDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_ids** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.filters_delete_request import FiltersDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersDeleteRequest from a JSON string
filters_delete_request_instance = FiltersDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(FiltersDeleteRequest.to_json())

# convert the object into a dict
filters_delete_request_dict = filters_delete_request_instance.to_dict()
# create an instance of FiltersDeleteRequest from a dict
filters_delete_request_from_dict = FiltersDeleteRequest.from_dict(filters_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


