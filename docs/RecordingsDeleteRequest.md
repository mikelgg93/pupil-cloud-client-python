# RecordingsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recording_ids** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.recordings_delete_request import RecordingsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingsDeleteRequest from a JSON string
recordings_delete_request_instance = RecordingsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(RecordingsDeleteRequest.to_json())

# convert the object into a dict
recordings_delete_request_dict = recordings_delete_request_instance.to_dict()
# create an instance of RecordingsDeleteRequest from a dict
recordings_delete_request_from_dict = RecordingsDeleteRequest.from_dict(recordings_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


