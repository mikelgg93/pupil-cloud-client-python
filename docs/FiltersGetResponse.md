# FiltersGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Filter]**](Filter.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.filters_get_response import FiltersGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersGetResponse from a JSON string
filters_get_response_instance = FiltersGetResponse.from_json(json)
# print the JSON string representation of the object
print(FiltersGetResponse.to_json())

# convert the object into a dict
filters_get_response_dict = filters_get_response_instance.to_dict()
# create an instance of FiltersGetResponse from a dict
filters_get_response_from_dict = FiltersGetResponse.from_dict(filters_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


