# RecordingEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**epoch_ns** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offset_s** | **float** |  | [optional] 
**origin** | **str** | origin of the event | 
**recording_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_event import RecordingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEvent from a JSON string
recording_event_instance = RecordingEvent.from_json(json)
# print the JSON string representation of the object
print(RecordingEvent.to_json())

# convert the object into a dict
recording_event_dict = recording_event_instance.to_dict()
# create an instance of RecordingEvent from a dict
recording_event_from_dict = RecordingEvent.from_dict(recording_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


