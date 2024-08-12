# SurfacePostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Surface**](Surface.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_post_response import SurfacePostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurfacePostResponse from a JSON string
surface_post_response_instance = SurfacePostResponse.from_json(json)
# print the JSON string representation of the object
print(SurfacePostResponse.to_json())

# convert the object into a dict
surface_post_response_dict = surface_post_response_instance.to_dict()
# create an instance of SurfacePostResponse from a dict
surface_post_response_from_dict = SurfacePostResponse.from_dict(surface_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


