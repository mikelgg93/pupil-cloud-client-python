# TokenPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Token**](Token.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.token_post_response import TokenPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPostResponse from a JSON string
token_post_response_instance = TokenPostResponse.from_json(json)
# print the JSON string representation of the object
print(TokenPostResponse.to_json())

# convert the object into a dict
token_post_response_dict = token_post_response_instance.to_dict()
# create an instance of TokenPostResponse from a dict
token_post_response_from_dict = TokenPostResponse.from_dict(token_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


