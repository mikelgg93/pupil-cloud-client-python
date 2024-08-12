# FaceDetectionTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_faces** | **float** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**max_faces** | **int** |  | [optional] 
**min_faces** | **int** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**total_frames** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.face_detection_timeline import FaceDetectionTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of FaceDetectionTimeline from a JSON string
face_detection_timeline_instance = FaceDetectionTimeline.from_json(json)
# print the JSON string representation of the object
print(FaceDetectionTimeline.to_json())

# convert the object into a dict
face_detection_timeline_dict = face_detection_timeline_instance.to_dict()
# create an instance of FaceDetectionTimeline from a dict
face_detection_timeline_from_dict = FaceDetectionTimeline.from_dict(face_detection_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


