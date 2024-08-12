# CreateRecordingEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**offset_s** | **float** | time offset within recording (seconds) | 

## Example

```python
from pupilcloud.models.create_recording_event import CreateRecordingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRecordingEvent from a JSON string
create_recording_event_instance = CreateRecordingEvent.from_json(json)
# print the JSON string representation of the object
print(CreateRecordingEvent.to_json())

# convert the object into a dict
create_recording_event_dict = create_recording_event_instance.to_dict()
# create an instance of CreateRecordingEvent from a dict
create_recording_event_from_dict = CreateRecordingEvent.from_dict(create_recording_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


