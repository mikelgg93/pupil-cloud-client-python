# TokenDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Token**](Token.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.token_delete_response import TokenDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDeleteResponse from a JSON string
token_delete_response_instance = TokenDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(TokenDeleteResponse.to_json())

# convert the object into a dict
token_delete_response_dict = token_delete_response_instance.to_dict()
# create an instance of TokenDeleteResponse from a dict
token_delete_response_from_dict = TokenDeleteResponse.from_dict(token_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


