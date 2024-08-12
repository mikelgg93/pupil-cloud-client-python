# WearersDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wearer_ids** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.wearers_delete_request import WearersDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WearersDeleteRequest from a JSON string
wearers_delete_request_instance = WearersDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(WearersDeleteRequest.to_json())

# convert the object into a dict
wearers_delete_request_dict = wearers_delete_request_instance.to_dict()
# create an instance of WearersDeleteRequest from a dict
wearers_delete_request_from_dict = WearersDeleteRequest.from_dict(wearers_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


