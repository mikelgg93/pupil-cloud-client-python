# GazeDatapoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blink_id** | **int** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**fixation_id** | **int** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**worn** | **int** |  | [optional] 
**x** | **int** |  | [optional] 
**y** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.gaze_datapoint import GazeDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of GazeDatapoint from a JSON string
gaze_datapoint_instance = GazeDatapoint.from_json(json)
# print the JSON string representation of the object
print(GazeDatapoint.to_json())

# convert the object into a dict
gaze_datapoint_dict = gaze_datapoint_instance.to_dict()
# create an instance of GazeDatapoint from a dict
gaze_datapoint_from_dict = GazeDatapoint.from_dict(gaze_datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


