# ApriltagResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distorted_apriltags** | **datetime** |  | [optional] 
**end_timestamp** | **float** |  | [optional] 
**normalized_apriltags** | **datetime** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.apriltag_result import ApriltagResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApriltagResult from a JSON string
apriltag_result_instance = ApriltagResult.from_json(json)
# print the JSON string representation of the object
print(ApriltagResult.to_json())

# convert the object into a dict
apriltag_result_dict = apriltag_result_instance.to_dict()
# create an instance of ApriltagResult from a dict
apriltag_result_from_dict = ApriltagResult.from_dict(apriltag_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


