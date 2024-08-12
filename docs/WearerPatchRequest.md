# WearerPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**ied** | **float** |  | [optional] 
**name** | **str** |  | 
**offset_correction** | [**OffsetCorrection**](OffsetCorrection.md) |  | [optional] 
**training_updated_on** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.wearer_patch_request import WearerPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WearerPatchRequest from a JSON string
wearer_patch_request_instance = WearerPatchRequest.from_json(json)
# print the JSON string representation of the object
print(WearerPatchRequest.to_json())

# convert the object into a dict
wearer_patch_request_dict = wearer_patch_request_instance.to_dict()
# create an instance of WearerPatchRequest from a dict
wearer_patch_request_from_dict = WearerPatchRequest.from_dict(wearer_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


