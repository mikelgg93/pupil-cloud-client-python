# Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_workspace_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] [readonly] 
**email_verified** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**onboarded_at** | **datetime** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**product_updates_subscribed** | **bool** |  | [optional] 
**provider** | **str** |  | [optional] [readonly] 
**uid** | **str** |  | [optional] [readonly] 
**user_workspaces** | [**List[WorkspaceMembership]**](WorkspaceMembership.md) |  | [optional] [readonly] 

## Example

```python
from pupilcloud.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


