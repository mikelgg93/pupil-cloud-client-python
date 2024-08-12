# RecordingFaceDetectionsTimelineGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[FaceDetectionTimeline]**](FaceDetectionTimeline.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_face_detections_timeline_get_response import RecordingFaceDetectionsTimelineGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFaceDetectionsTimelineGetResponse from a JSON string
recording_face_detections_timeline_get_response_instance = RecordingFaceDetectionsTimelineGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingFaceDetectionsTimelineGetResponse.to_json())

# convert the object into a dict
recording_face_detections_timeline_get_response_dict = recording_face_detections_timeline_get_response_instance.to_dict()
# create an instance of RecordingFaceDetectionsTimelineGetResponse from a dict
recording_face_detections_timeline_get_response_from_dict = RecordingFaceDetectionsTimelineGetResponse.from_dict(recording_face_detections_timeline_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


