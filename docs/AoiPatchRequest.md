# AoiPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounding_box** | **str** |  | [optional] 
**centroid_xy** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrichment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mask_image_data_url** | **str** |  | [optional] 
**name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.aoi_patch_request import AoiPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AoiPatchRequest from a JSON string
aoi_patch_request_instance = AoiPatchRequest.from_json(json)
# print the JSON string representation of the object
print(AoiPatchRequest.to_json())

# convert the object into a dict
aoi_patch_request_dict = aoi_patch_request_instance.to_dict()
# create an instance of AoiPatchRequest from a dict
aoi_patch_request_from_dict = AoiPatchRequest.from_dict(aoi_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


