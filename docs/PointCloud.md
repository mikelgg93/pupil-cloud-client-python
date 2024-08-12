# PointCloud


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**z** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.point_cloud import PointCloud

# TODO update the JSON string below
json = "{}"
# create an instance of PointCloud from a JSON string
point_cloud_instance = PointCloud.from_json(json)
# print the JSON string representation of the object
print(PointCloud.to_json())

# convert the object into a dict
point_cloud_dict = point_cloud_instance.to_dict()
# create an instance of PointCloud from a dict
point_cloud_from_dict = PointCloud.from_dict(point_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


