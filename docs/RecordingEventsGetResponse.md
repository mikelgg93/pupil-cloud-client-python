# RecordingEventsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[RecordingEvent]**](RecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_events_get_response import RecordingEventsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEventsGetResponse from a JSON string
recording_events_get_response_instance = RecordingEventsGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingEventsGetResponse.to_json())

# convert the object into a dict
recording_events_get_response_dict = recording_events_get_response_instance.to_dict()
# create an instance of RecordingEventsGetResponse from a dict
recording_events_get_response_from_dict = RecordingEventsGetResponse.from_dict(recording_events_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


