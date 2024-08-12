# LogoutPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Profile**](Profile.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.logout_post_response import LogoutPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LogoutPostResponse from a JSON string
logout_post_response_instance = LogoutPostResponse.from_json(json)
# print the JSON string representation of the object
print(LogoutPostResponse.to_json())

# convert the object into a dict
logout_post_response_dict = logout_post_response_instance.to_dict()
# create an instance of LogoutPostResponse from a dict
logout_post_response_from_dict = LogoutPostResponse.from_dict(logout_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


