# RecordingEventResourceDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**RecordingEvent**](RecordingEvent.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_event_resource_delete_response import RecordingEventResourceDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingEventResourceDeleteResponse from a JSON string
recording_event_resource_delete_response_instance = RecordingEventResourceDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingEventResourceDeleteResponse.to_json())

# convert the object into a dict
recording_event_resource_delete_response_dict = recording_event_resource_delete_response_instance.to_dict()
# create an instance of RecordingEventResourceDeleteResponse from a dict
recording_event_resource_delete_response_from_dict = RecordingEventResourceDeleteResponse.from_dict(recording_event_resource_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


