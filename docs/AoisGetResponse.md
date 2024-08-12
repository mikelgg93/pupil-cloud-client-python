# AoisGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[AoisResponse]**](AoisResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.aois_get_response import AoisGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AoisGetResponse from a JSON string
aois_get_response_instance = AoisGetResponse.from_json(json)
# print the JSON string representation of the object
print(AoisGetResponse.to_json())

# convert the object into a dict
aois_get_response_dict = aois_get_response_instance.to_dict()
# create an instance of AoisGetResponse from a dict
aois_get_response_from_dict = AoisGetResponse.from_dict(aois_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


