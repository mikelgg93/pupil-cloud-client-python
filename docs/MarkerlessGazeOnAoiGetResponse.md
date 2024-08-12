# MarkerlessGazeOnAoiGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[GazeOnAoi]**](GazeOnAoi.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.markerless_gaze_on_aoi_get_response import MarkerlessGazeOnAoiGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessGazeOnAoiGetResponse from a JSON string
markerless_gaze_on_aoi_get_response_instance = MarkerlessGazeOnAoiGetResponse.from_json(json)
# print the JSON string representation of the object
print(MarkerlessGazeOnAoiGetResponse.to_json())

# convert the object into a dict
markerless_gaze_on_aoi_get_response_dict = markerless_gaze_on_aoi_get_response_instance.to_dict()
# create an instance of MarkerlessGazeOnAoiGetResponse from a dict
markerless_gaze_on_aoi_get_response_from_dict = MarkerlessGazeOnAoiGetResponse.from_dict(markerless_gaze_on_aoi_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


