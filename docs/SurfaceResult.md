# SurfaceResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corners** | **datetime** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**marker_ids** | **List[str]** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.surface_result import SurfaceResult

# TODO update the JSON string below
json = "{}"
# create an instance of SurfaceResult from a JSON string
surface_result_instance = SurfaceResult.from_json(json)
# print the JSON string representation of the object
print(SurfaceResult.to_json())

# convert the object into a dict
surface_result_dict = surface_result_instance.to_dict()
# create an instance of SurfaceResult from a dict
surface_result_from_dict = SurfaceResult.from_dict(surface_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


