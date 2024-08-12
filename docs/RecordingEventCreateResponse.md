# RecordingEventCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**CreateRecordingEvent**](CreateRecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_event_create_response import RecordingEventCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEventCreateResponse from a JSON string
recording_event_create_response_instance = RecordingEventCreateResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingEventCreateResponse.to_json())

# convert the object into a dict
recording_event_create_response_dict = recording_event_create_response_instance.to_dict()
# create an instance of RecordingEventCreateResponse from a dict
recording_event_create_response_from_dict = RecordingEventCreateResponse.from_dict(recording_event_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


