# TokensGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Token]**](Token.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.tokens_get_response import TokensGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokensGetResponse from a JSON string
tokens_get_response_instance = TokensGetResponse.from_json(json)
# print the JSON string representation of the object
print(TokensGetResponse.to_json())

# convert the object into a dict
tokens_get_response_dict = tokens_get_response_instance.to_dict()
# create an instance of TokensGetResponse from a dict
tokens_get_response_from_dict = TokensGetResponse.from_dict(tokens_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


