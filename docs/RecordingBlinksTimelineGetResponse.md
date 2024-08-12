# RecordingBlinksTimelineGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[BlinksTimeline]**](BlinksTimeline.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_blinks_timeline_get_response import RecordingBlinksTimelineGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingBlinksTimelineGetResponse from a JSON string
recording_blinks_timeline_get_response_instance = RecordingBlinksTimelineGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingBlinksTimelineGetResponse.to_json())

# convert the object into a dict
recording_blinks_timeline_get_response_dict = recording_blinks_timeline_get_response_instance.to_dict()
# create an instance of RecordingBlinksTimelineGetResponse from a dict
recording_blinks_timeline_get_response_from_dict = RecordingBlinksTimelineGetResponse.from_dict(recording_blinks_timeline_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


