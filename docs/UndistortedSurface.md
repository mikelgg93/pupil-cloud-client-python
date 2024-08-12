# UndistortedSurface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corners** | **datetime** |  | [optional] 
**marker_ids** | **List[str]** |  | [optional] 
**ts** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.undistorted_surface import UndistortedSurface

# TODO update the JSON string below
json = "{}"
# create an instance of UndistortedSurface from a JSON string
undistorted_surface_instance = UndistortedSurface.from_json(json)
# print the JSON string representation of the object
print(UndistortedSurface.to_json())

# convert the object into a dict
undistorted_surface_dict = undistorted_surface_instance.to_dict()
# create an instance of UndistortedSurface from a dict
undistorted_surface_from_dict = UndistortedSurface.from_dict(undistorted_surface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


