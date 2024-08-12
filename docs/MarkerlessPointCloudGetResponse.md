# MarkerlessPointCloudGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[PointCloud]**](PointCloud.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.markerless_point_cloud_get_response import MarkerlessPointCloudGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessPointCloudGetResponse from a JSON string
markerless_point_cloud_get_response_instance = MarkerlessPointCloudGetResponse.from_json(json)
# print the JSON string representation of the object
print(MarkerlessPointCloudGetResponse.to_json())

# convert the object into a dict
markerless_point_cloud_get_response_dict = markerless_point_cloud_get_response_instance.to_dict()
# create an instance of MarkerlessPointCloudGetResponse from a dict
markerless_point_cloud_get_response_from_dict = MarkerlessPointCloudGetResponse.from_dict(markerless_point_cloud_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


