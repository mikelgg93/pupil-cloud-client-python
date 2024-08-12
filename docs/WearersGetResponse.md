# WearersGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Wearer]**](Wearer.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.wearers_get_response import WearersGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WearersGetResponse from a JSON string
wearers_get_response_instance = WearersGetResponse.from_json(json)
# print the JSON string representation of the object
print(WearersGetResponse.to_json())

# convert the object into a dict
wearers_get_response_dict = wearers_get_response_instance.to_dict()
# create an instance of WearersGetResponse from a dict
wearers_get_response_from_dict = WearersGetResponse.from_dict(wearers_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


