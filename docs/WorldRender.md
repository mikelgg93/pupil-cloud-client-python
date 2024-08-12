# WorldRender


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audio** | **bool** |  | [optional] [default to True]
**gaze_circle** | [**GazeCircle**](GazeCircle.md) |  | [optional] 
**id** | **str** |  | [optional] 
**undistort_frames** | **bool** |  | [optional] [default to False]
**with_gaze** | **bool** |  | [optional] [default to True]
**with_scanpath** | **bool** |  | [optional] [default to False]
**with_timestamps** | **bool** |  | [optional] [default to False]

## Example

```python
from pupilcloud.models.world_render import WorldRender

# TODO update the JSON string below
json = "{}"
# create an instance of WorldRender from a JSON string
world_render_instance = WorldRender.from_json(json)
# print the JSON string representation of the object
print(WorldRender.to_json())

# convert the object into a dict
world_render_dict = world_render_instance.to_dict()
# create an instance of WorldRender from a dict
world_render_from_dict = WorldRender.from_dict(world_render_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


