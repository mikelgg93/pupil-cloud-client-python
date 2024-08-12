# SurfaceCornersGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[SurfaceResult]**](SurfaceResult.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_corners_get_response import SurfaceCornersGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurfaceCornersGetResponse from a JSON string
surface_corners_get_response_instance = SurfaceCornersGetResponse.from_json(json)
# print the JSON string representation of the object
print(SurfaceCornersGetResponse.to_json())

# convert the object into a dict
surface_corners_get_response_dict = surface_corners_get_response_instance.to_dict()
# create an instance of SurfaceCornersGetResponse from a dict
surface_corners_get_response_from_dict = SurfaceCornersGetResponse.from_dict(surface_corners_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


