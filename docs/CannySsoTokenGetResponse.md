# CannySsoTokenGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**CannySSOToken**](CannySSOToken.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.canny_sso_token_get_response import CannySsoTokenGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CannySsoTokenGetResponse from a JSON string
canny_sso_token_get_response_instance = CannySsoTokenGetResponse.from_json(json)
# print the JSON string representation of the object
print(CannySsoTokenGetResponse.to_json())

# convert the object into a dict
canny_sso_token_get_response_dict = canny_sso_token_get_response_instance.to_dict()
# create an instance of CannySsoTokenGetResponse from a dict
canny_sso_token_get_response_from_dict = CannySsoTokenGetResponse.from_dict(canny_sso_token_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


