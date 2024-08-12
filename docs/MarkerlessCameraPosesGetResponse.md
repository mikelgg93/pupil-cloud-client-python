# MarkerlessCameraPosesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[CameraPose]**](CameraPose.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.markerless_camera_poses_get_response import MarkerlessCameraPosesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessCameraPosesGetResponse from a JSON string
markerless_camera_poses_get_response_instance = MarkerlessCameraPosesGetResponse.from_json(json)
# print the JSON string representation of the object
print(MarkerlessCameraPosesGetResponse.to_json())

# convert the object into a dict
markerless_camera_poses_get_response_dict = markerless_camera_poses_get_response_instance.to_dict()
# create an instance of MarkerlessCameraPosesGetResponse from a dict
markerless_camera_poses_get_response_from_dict = MarkerlessCameraPosesGetResponse.from_dict(markerless_camera_poses_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


