# LoginPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Profile**](Profile.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.login_post_response import LoginPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LoginPostResponse from a JSON string
login_post_response_instance = LoginPostResponse.from_json(json)
# print the JSON string representation of the object
print(LoginPostResponse.to_json())

# convert the object into a dict
login_post_response_dict = login_post_response_instance.to_dict()
# create an instance of LoginPostResponse from a dict
login_post_response_from_dict = LoginPostResponse.from_dict(login_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


