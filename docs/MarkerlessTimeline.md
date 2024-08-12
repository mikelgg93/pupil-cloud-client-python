# MarkerlessTimeline


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
from pupilcloud.models.markerless_timeline import MarkerlessTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessTimeline from a JSON string
markerless_timeline_instance = MarkerlessTimeline.from_json(json)
# print the JSON string representation of the object
print(MarkerlessTimeline.to_json())

# convert the object into a dict
markerless_timeline_dict = markerless_timeline_instance.to_dict()
# create an instance of MarkerlessTimeline from a dict
markerless_timeline_from_dict = MarkerlessTimeline.from_dict(markerless_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


