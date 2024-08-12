# SurfaceGazeOnAoiGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[GazeOnAoi]**](GazeOnAoi.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_gaze_on_aoi_get_response import SurfaceGazeOnAoiGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurfaceGazeOnAoiGetResponse from a JSON string
surface_gaze_on_aoi_get_response_instance = SurfaceGazeOnAoiGetResponse.from_json(json)
# print the JSON string representation of the object
print(SurfaceGazeOnAoiGetResponse.to_json())

# convert the object into a dict
surface_gaze_on_aoi_get_response_dict = surface_gaze_on_aoi_get_response_instance.to_dict()
# create an instance of SurfaceGazeOnAoiGetResponse from a dict
surface_gaze_on_aoi_get_response_from_dict = SurfaceGazeOnAoiGetResponse.from_dict(surface_gaze_on_aoi_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


