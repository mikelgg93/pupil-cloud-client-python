# MarkerlessDetectionsTimelineGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[MarkerlessTimeline]**](MarkerlessTimeline.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.markerless_detections_timeline_get_response import MarkerlessDetectionsTimelineGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessDetectionsTimelineGetResponse from a JSON string
markerless_detections_timeline_get_response_instance = MarkerlessDetectionsTimelineGetResponse.from_json(json)
# print the JSON string representation of the object
print(MarkerlessDetectionsTimelineGetResponse.to_json())

# convert the object into a dict
markerless_detections_timeline_get_response_dict = markerless_detections_timeline_get_response_instance.to_dict()
# create an instance of MarkerlessDetectionsTimelineGetResponse from a dict
markerless_detections_timeline_get_response_from_dict = MarkerlessDetectionsTimelineGetResponse.from_dict(markerless_detections_timeline_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


