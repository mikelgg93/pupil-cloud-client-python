# Scanpath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**path** | [**List[ScanpathPoint]**](ScanpathPoint.md) |  | [optional] 
**start_timestamp** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.scanpath import Scanpath

# TODO update the JSON string below
json = "{}"
# create an instance of Scanpath from a JSON string
scanpath_instance = Scanpath.from_json(json)
# print the JSON string representation of the object
print(Scanpath.to_json())

# convert the object into a dict
scanpath_dict = scanpath_instance.to_dict()
# create an instance of Scanpath from a dict
scanpath_from_dict = Scanpath.from_dict(scanpath_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


