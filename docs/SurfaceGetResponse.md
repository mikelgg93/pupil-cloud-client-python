# SurfaceGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Surface**](Surface.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_get_response import SurfaceGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurfaceGetResponse from a JSON string
surface_get_response_instance = SurfaceGetResponse.from_json(json)
# print the JSON string representation of the object
print(SurfaceGetResponse.to_json())

# convert the object into a dict
surface_get_response_dict = surface_get_response_instance.to_dict()
# create an instance of SurfaceGetResponse from a dict
surface_get_response_from_dict = SurfaceGetResponse.from_dict(surface_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


