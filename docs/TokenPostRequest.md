# TokenPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from pupilcloud.models.token_post_request import TokenPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPostRequest from a JSON string
token_post_request_instance = TokenPostRequest.from_json(json)
# print the JSON string representation of the object
print(TokenPostRequest.to_json())

# convert the object into a dict
token_post_request_dict = token_post_request_instance.to_dict()
# create an instance of TokenPostRequest from a dict
token_post_request_from_dict = TokenPostRequest.from_dict(token_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


