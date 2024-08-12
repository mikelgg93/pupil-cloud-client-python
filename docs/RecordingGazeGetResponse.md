# RecordingGazeGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[GazeDatapoint]**](GazeDatapoint.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_gaze_get_response import RecordingGazeGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingGazeGetResponse from a JSON string
recording_gaze_get_response_instance = RecordingGazeGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingGazeGetResponse.to_json())

# convert the object into a dict
recording_gaze_get_response_dict = recording_gaze_get_response_instance.to_dict()
# create an instance of RecordingGazeGetResponse from a dict
recording_gaze_get_response_from_dict = RecordingGazeGetResponse.from_dict(recording_gaze_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


