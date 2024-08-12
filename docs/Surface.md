# Surface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_initialized** | **bool** |  | [optional] 
**markers_used** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.surface import Surface

# TODO update the JSON string below
json = "{}"
# create an instance of Surface from a JSON string
surface_instance = Surface.from_json(json)
# print the JSON string representation of the object
print(Surface.to_json())

# convert the object into a dict
surface_dict = surface_instance.to_dict()
# create an instance of Surface from a dict
surface_from_dict = Surface.from_dict(surface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


