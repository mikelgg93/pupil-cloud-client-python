# SurfacePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Surface**](Surface.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_patch_response import SurfacePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurfacePatchResponse from a JSON string
surface_patch_response_instance = SurfacePatchResponse.from_json(json)
# print the JSON string representation of the object
print(SurfacePatchResponse.to_json())

# convert the object into a dict
surface_patch_response_dict = surface_patch_response_instance.to_dict()
# create an instance of SurfacePatchResponse from a dict
surface_patch_response_from_dict = SurfacePatchResponse.from_dict(surface_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


