# WearerGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Wearer**](Wearer.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.wearer_get_response import WearerGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WearerGetResponse from a JSON string
wearer_get_response_instance = WearerGetResponse.from_json(json)
# print the JSON string representation of the object
print(WearerGetResponse.to_json())

# convert the object into a dict
wearer_get_response_dict = wearer_get_response_instance.to_dict()
# create an instance of WearerGetResponse from a dict
wearer_get_response_from_dict = WearerGetResponse.from_dict(wearer_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


