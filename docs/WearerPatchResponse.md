# WearerPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Wearer**](Wearer.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.wearer_patch_response import WearerPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WearerPatchResponse from a JSON string
wearer_patch_response_instance = WearerPatchResponse.from_json(json)
# print the JSON string representation of the object
print(WearerPatchResponse.to_json())

# convert the object into a dict
wearer_patch_response_dict = wearer_patch_response_instance.to_dict()
# create an instance of WearerPatchResponse from a dict
wearer_patch_response_from_dict = WearerPatchResponse.from_dict(wearer_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


