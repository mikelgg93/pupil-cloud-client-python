# ProfilePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Profile**](Profile.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.profile_patch_response import ProfilePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePatchResponse from a JSON string
profile_patch_response_instance = ProfilePatchResponse.from_json(json)
# print the JSON string representation of the object
print(ProfilePatchResponse.to_json())

# convert the object into a dict
profile_patch_response_dict = profile_patch_response_instance.to_dict()
# create an instance of ProfilePatchResponse from a dict
profile_patch_response_from_dict = ProfilePatchResponse.from_dict(profile_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


