# ProfileGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Profile**](Profile.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.profile_get_response import ProfileGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGetResponse from a JSON string
profile_get_response_instance = ProfileGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProfileGetResponse.to_json())

# convert the object into a dict
profile_get_response_dict = profile_get_response_instance.to_dict()
# create an instance of ProfileGetResponse from a dict
profile_get_response_from_dict = ProfileGetResponse.from_dict(profile_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


