# RecordingEventPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**offset_s** | **float** | time offset within recording (seconds) | [optional] 

## Example

```python
from pupilcloud.models.recording_event_patch_request import RecordingEventPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEventPatchRequest from a JSON string
recording_event_patch_request_instance = RecordingEventPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RecordingEventPatchRequest.to_json())

# convert the object into a dict
recording_event_patch_request_dict = recording_event_patch_request_instance.to_dict()
# create an instance of RecordingEventPatchRequest from a dict
recording_event_patch_request_from_dict = RecordingEventPatchRequest.from_dict(recording_event_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


