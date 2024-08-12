# GazeCircle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**Color**](Color.md) |  | [optional] 
**radius** | **int** |  | [optional] 
**stroke_width** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.gaze_circle import GazeCircle

# TODO update the JSON string below
json = "{}"
# create an instance of GazeCircle from a JSON string
gaze_circle_instance = GazeCircle.from_json(json)
# print the JSON string representation of the object
print(GazeCircle.to_json())

# convert the object into a dict
gaze_circle_dict = gaze_circle_instance.to_dict()
# create an instance of GazeCircle from a dict
gaze_circle_from_dict = GazeCircle.from_dict(gaze_circle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


