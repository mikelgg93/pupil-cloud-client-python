# AoiPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**AoisResponse**](AoisResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.aoi_patch_response import AoiPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AoiPatchResponse from a JSON string
aoi_patch_response_instance = AoiPatchResponse.from_json(json)
# print the JSON string representation of the object
print(AoiPatchResponse.to_json())

# convert the object into a dict
aoi_patch_response_dict = aoi_patch_response_instance.to_dict()
# create an instance of AoiPatchResponse from a dict
aoi_patch_response_from_dict = AoiPatchResponse.from_dict(aoi_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


