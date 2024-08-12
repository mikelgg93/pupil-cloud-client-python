# AoiGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**AoisResponse**](AoisResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.aoi_get_response import AoiGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AoiGetResponse from a JSON string
aoi_get_response_instance = AoiGetResponse.from_json(json)
# print the JSON string representation of the object
print(AoiGetResponse.to_json())

# convert the object into a dict
aoi_get_response_dict = aoi_get_response_instance.to_dict()
# create an instance of AoiGetResponse from a dict
aoi_get_response_from_dict = AoiGetResponse.from_dict(aoi_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


