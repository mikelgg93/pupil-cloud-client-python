# WearerDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Wearer**](Wearer.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.wearer_delete_response import WearerDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WearerDeleteResponse from a JSON string
wearer_delete_response_instance = WearerDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(WearerDeleteResponse.to_json())

# convert the object into a dict
wearer_delete_response_dict = wearer_delete_response_instance.to_dict()
# create an instance of WearerDeleteResponse from a dict
wearer_delete_response_from_dict = WearerDeleteResponse.from_dict(wearer_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


