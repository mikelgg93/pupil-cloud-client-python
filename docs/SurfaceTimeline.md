# SurfaceTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aoi_detected** | **float** |  | [optional] 
**avg_gaze_on_aoi** | **float** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**gaze_on_aoi** | **float** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**sum_gaze_on_aoi** | **int** |  | [optional] 
**total_frames** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_timeline import SurfaceTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of SurfaceTimeline from a JSON string
surface_timeline_instance = SurfaceTimeline.from_json(json)
# print the JSON string representation of the object
print(SurfaceTimeline.to_json())

# convert the object into a dict
surface_timeline_dict = surface_timeline_instance.to_dict()
# create an instance of SurfaceTimeline from a dict
surface_timeline_from_dict = SurfaceTimeline.from_dict(surface_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


