# CannySSOToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.canny_sso_token import CannySSOToken

# TODO update the JSON string below
json = "{}"
# create an instance of CannySSOToken from a JSON string
canny_sso_token_instance = CannySSOToken.from_json(json)
# print the JSON string representation of the object
print(CannySSOToken.to_json())

# convert the object into a dict
canny_sso_token_dict = canny_sso_token_instance.to_dict()
# create an instance of CannySSOToken from a dict
canny_sso_token_from_dict = CannySSOToken.from_dict(canny_sso_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


