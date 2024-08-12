# SetDistortedSurfaceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corners** | **datetime** |  | [optional] 
**markers_used** | **List[str]** |  | 
**recording_id** | **str** |  | 
**timestamp** | **float** |  | 

## Example

```python
from pupilcloud.models.set_distorted_surface_request import SetDistortedSurfaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDistortedSurfaceRequest from a JSON string
set_distorted_surface_request_instance = SetDistortedSurfaceRequest.from_json(json)
# print the JSON string representation of the object
print(SetDistortedSurfaceRequest.to_json())

# convert the object into a dict
set_distorted_surface_request_dict = set_distorted_surface_request_instance.to_dict()
# create an instance of SetDistortedSurfaceRequest from a dict
set_distorted_surface_request_from_dict = SetDistortedSurfaceRequest.from_dict(set_distorted_surface_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


