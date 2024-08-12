# RecordingEventPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**RecordingEvent**](RecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_event_post_response import RecordingEventPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEventPostResponse from a JSON string
recording_event_post_response_instance = RecordingEventPostResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingEventPostResponse.to_json())

# convert the object into a dict
recording_event_post_response_dict = recording_event_post_response_instance.to_dict()
# create an instance of RecordingEventPostResponse from a dict
recording_event_post_response_from_dict = RecordingEventPostResponse.from_dict(recording_event_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


