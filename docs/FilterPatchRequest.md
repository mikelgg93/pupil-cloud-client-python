# FilterPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**filter_query** | **str** |  | [optional] 
**filter_scope** | **str** | the scope of the filter | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** | the filter syntax kind | [optional] [default to 'lucene']
**name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.filter_patch_request import FilterPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterPatchRequest from a JSON string
filter_patch_request_instance = FilterPatchRequest.from_json(json)
# print the JSON string representation of the object
print(FilterPatchRequest.to_json())

# convert the object into a dict
filter_patch_request_dict = filter_patch_request_instance.to_dict()
# create an instance of FilterPatchRequest from a dict
filter_patch_request_from_dict = FilterPatchRequest.from_dict(filter_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


