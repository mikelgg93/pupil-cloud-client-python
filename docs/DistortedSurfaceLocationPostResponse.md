# DistortedSurfaceLocationPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**UndistortedSurface**](UndistortedSurface.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.distorted_surface_location_post_response import DistortedSurfaceLocationPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DistortedSurfaceLocationPostResponse from a JSON string
distorted_surface_location_post_response_instance = DistortedSurfaceLocationPostResponse.from_json(json)
# print the JSON string representation of the object
print(DistortedSurfaceLocationPostResponse.to_json())

# convert the object into a dict
distorted_surface_location_post_response_dict = distorted_surface_location_post_response_instance.to_dict()
# create an instance of DistortedSurfaceLocationPostResponse from a dict
distorted_surface_location_post_response_from_dict = DistortedSurfaceLocationPostResponse.from_dict(distorted_surface_location_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


