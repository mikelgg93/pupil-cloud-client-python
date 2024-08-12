# RecordingSceneCameraIntrinsicsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**SceneCameraIntrinsics**](SceneCameraIntrinsics.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_scene_camera_intrinsics_get_response import RecordingSceneCameraIntrinsicsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingSceneCameraIntrinsicsGetResponse from a JSON string
recording_scene_camera_intrinsics_get_response_instance = RecordingSceneCameraIntrinsicsGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingSceneCameraIntrinsicsGetResponse.to_json())

# convert the object into a dict
recording_scene_camera_intrinsics_get_response_dict = recording_scene_camera_intrinsics_get_response_instance.to_dict()
# create an instance of RecordingSceneCameraIntrinsicsGetResponse from a dict
recording_scene_camera_intrinsics_get_response_from_dict = RecordingSceneCameraIntrinsicsGetResponse.from_dict(recording_scene_camera_intrinsics_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


