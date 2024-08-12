# GazeOnAoi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**fixation_id** | **int** |  | [optional] 
**gaze_in_aoi_x** | **float** |  | [optional] 
**gaze_in_aoi_y** | **float** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.gaze_on_aoi import GazeOnAoi

# TODO update the JSON string below
json = "{}"
# create an instance of GazeOnAoi from a JSON string
gaze_on_aoi_instance = GazeOnAoi.from_json(json)
# print the JSON string representation of the object
print(GazeOnAoi.to_json())

# convert the object into a dict
gaze_on_aoi_dict = gaze_on_aoi_instance.to_dict()
# create an instance of GazeOnAoi from a dict
gaze_on_aoi_from_dict = GazeOnAoi.from_dict(gaze_on_aoi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


