# WearerPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Wearer**](Wearer.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.wearer_post_response import WearerPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WearerPostResponse from a JSON string
wearer_post_response_instance = WearerPostResponse.from_json(json)
# print the JSON string representation of the object
print(WearerPostResponse.to_json())

# convert the object into a dict
wearer_post_response_dict = wearer_post_response_instance.to_dict()
# create an instance of WearerPostResponse from a dict
wearer_post_response_from_dict = WearerPostResponse.from_dict(wearer_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


