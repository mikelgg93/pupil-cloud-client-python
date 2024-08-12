# AoiPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**AoisResponse**](AoisResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.aoi_post_response import AoiPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AoiPostResponse from a JSON string
aoi_post_response_instance = AoiPostResponse.from_json(json)
# print the JSON string representation of the object
print(AoiPostResponse.to_json())

# convert the object into a dict
aoi_post_response_dict = aoi_post_response_instance.to_dict()
# create an instance of AoiPostResponse from a dict
aoi_post_response_from_dict = AoiPostResponse.from_dict(aoi_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


