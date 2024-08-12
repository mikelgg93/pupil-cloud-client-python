# AoiPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounding_box** | **str** |  | [optional] 
**centroid_xy** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**enrichment_id** | **str** |  | 
**id** | **str** |  | [optional] 
**mask_image_data_url** | **str** |  | [optional] 
**name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.aoi_post_request import AoiPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AoiPostRequest from a JSON string
aoi_post_request_instance = AoiPostRequest.from_json(json)
# print the JSON string representation of the object
print(AoiPostRequest.to_json())

# convert the object into a dict
aoi_post_request_dict = aoi_post_request_instance.to_dict()
# create an instance of AoiPostRequest from a dict
aoi_post_request_from_dict = AoiPostRequest.from_dict(aoi_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


