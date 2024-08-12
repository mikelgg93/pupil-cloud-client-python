# FiltersPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Filter**](Filter.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.filters_post_response import FiltersPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FiltersPostResponse from a JSON string
filters_post_response_instance = FiltersPostResponse.from_json(json)
# print the JSON string representation of the object
print(FiltersPostResponse.to_json())

# convert the object into a dict
filters_post_response_dict = filters_post_response_instance.to_dict()
# create an instance of FiltersPostResponse from a dict
filters_post_response_from_dict = FiltersPostResponse.from_dict(filters_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


