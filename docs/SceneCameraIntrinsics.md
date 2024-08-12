# SceneCameraIntrinsics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**camera_matrix** | **List[List[float]]** |  | [optional] 
**dist_coefs** | **List[List[float]]** |  | [optional] 
**rotation_matrix** | **List[List[float]]** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.scene_camera_intrinsics import SceneCameraIntrinsics

# TODO update the JSON string below
json = "{}"
# create an instance of SceneCameraIntrinsics from a JSON string
scene_camera_intrinsics_instance = SceneCameraIntrinsics.from_json(json)
# print the JSON string representation of the object
print(SceneCameraIntrinsics.to_json())

# convert the object into a dict
scene_camera_intrinsics_dict = scene_camera_intrinsics_instance.to_dict()
# create an instance of SceneCameraIntrinsics from a dict
scene_camera_intrinsics_from_dict = SceneCameraIntrinsics.from_dict(scene_camera_intrinsics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


