# CameraPose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**rotation_x** | **float** |  | [optional] 
**rotation_y** | **float** |  | [optional] 
**rotation_z** | **float** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**translation_x** | **float** |  | [optional] 
**translation_y** | **float** |  | [optional] 
**translation_z** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.camera_pose import CameraPose

# TODO update the JSON string below
json = "{}"
# create an instance of CameraPose from a JSON string
camera_pose_instance = CameraPose.from_json(json)
# print the JSON string representation of the object
print(CameraPose.to_json())

# convert the object into a dict
camera_pose_dict = camera_pose_instance.to_dict()
# create an instance of CameraPose from a dict
camera_pose_from_dict = CameraPose.from_dict(camera_pose_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


