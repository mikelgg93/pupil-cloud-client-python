# RecordingEventPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**offset_s** | **float** | time offset within recording (seconds) | 

## Example

```python
from pupilcloud.models.recording_event_post_request import RecordingEventPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEventPostRequest from a JSON string
recording_event_post_request_instance = RecordingEventPostRequest.from_json(json)
# print the JSON string representation of the object
print(RecordingEventPostRequest.to_json())

# convert the object into a dict
recording_event_post_request_dict = recording_event_post_request_instance.to_dict()
# create an instance of RecordingEventPostRequest from a dict
recording_event_post_request_from_dict = RecordingEventPostRequest.from_dict(recording_event_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


