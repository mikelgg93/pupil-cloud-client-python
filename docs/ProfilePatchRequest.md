# ProfilePatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**onboarded** | **bool** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**product_updates_subscribed** | **bool** |  | [optional] 

## Example

```python
from pupilcloud.models.profile_patch_request import ProfilePatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilePatchRequest from a JSON string
profile_patch_request_instance = ProfilePatchRequest.from_json(json)
# print the JSON string representation of the object
print(ProfilePatchRequest.to_json())

# convert the object into a dict
profile_patch_request_dict = profile_patch_request_instance.to_dict()
# create an instance of ProfilePatchRequest from a dict
profile_patch_request_from_dict = ProfilePatchRequest.from_dict(profile_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


