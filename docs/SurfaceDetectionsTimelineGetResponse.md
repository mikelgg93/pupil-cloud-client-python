# SurfaceDetectionsTimelineGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[SurfaceTimeline]**](SurfaceTimeline.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_detections_timeline_get_response import SurfaceDetectionsTimelineGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurfaceDetectionsTimelineGetResponse from a JSON string
surface_detections_timeline_get_response_instance = SurfaceDetectionsTimelineGetResponse.from_json(json)
# print the JSON string representation of the object
print(SurfaceDetectionsTimelineGetResponse.to_json())

# convert the object into a dict
surface_detections_timeline_get_response_dict = surface_detections_timeline_get_response_instance.to_dict()
# create an instance of SurfaceDetectionsTimelineGetResponse from a dict
surface_detections_timeline_get_response_from_dict = SurfaceDetectionsTimelineGetResponse.from_dict(surface_detections_timeline_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


