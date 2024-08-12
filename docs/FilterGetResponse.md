# FilterGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Filter**](Filter.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.filter_get_response import FilterGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterGetResponse from a JSON string
filter_get_response_instance = FilterGetResponse.from_json(json)
# print the JSON string representation of the object
print(FilterGetResponse.to_json())

# convert the object into a dict
filter_get_response_dict = filter_get_response_instance.to_dict()
# create an instance of FilterGetResponse from a dict
filter_get_response_from_dict = FilterGetResponse.from_dict(filter_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


