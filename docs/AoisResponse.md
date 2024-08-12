# AoisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bounding_box** | **str** |  | [optional] 
**centroid_xy** | **str** |  | [optional] 
**color** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrichment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mask_image_data_url** | **str** |  | [optional] 
**name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.aois_response import AoisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AoisResponse from a JSON string
aois_response_instance = AoisResponse.from_json(json)
# print the JSON string representation of the object
print(AoisResponse.to_json())

# convert the object into a dict
aois_response_dict = aois_response_instance.to_dict()
# create an instance of AoisResponse from a dict
aois_response_from_dict = AoisResponse.from_dict(aois_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


