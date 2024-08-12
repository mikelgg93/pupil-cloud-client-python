# FilterPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Filter**](Filter.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.filter_patch_response import FilterPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FilterPatchResponse from a JSON string
filter_patch_response_instance = FilterPatchResponse.from_json(json)
# print the JSON string representation of the object
print(FilterPatchResponse.to_json())

# convert the object into a dict
filter_patch_response_dict = filter_patch_response_instance.to_dict()
# create an instance of FilterPatchResponse from a dict
filter_patch_response_from_dict = FilterPatchResponse.from_dict(filter_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


