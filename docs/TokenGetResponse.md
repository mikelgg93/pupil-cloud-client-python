# TokenGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Token**](Token.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.token_get_response import TokenGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenGetResponse from a JSON string
token_get_response_instance = TokenGetResponse.from_json(json)
# print the JSON string representation of the object
print(TokenGetResponse.to_json())

# convert the object into a dict
token_get_response_dict = token_get_response_instance.to_dict()
# create an instance of TokenGetResponse from a dict
token_get_response_from_dict = TokenGetResponse.from_dict(token_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


