# ApriltagDetectionsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[ApriltagResult]**](ApriltagResult.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.apriltag_detections_get_response import ApriltagDetectionsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApriltagDetectionsGetResponse from a JSON string
apriltag_detections_get_response_instance = ApriltagDetectionsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ApriltagDetectionsGetResponse.to_json())

# convert the object into a dict
apriltag_detections_get_response_dict = apriltag_detections_get_response_instance.to_dict()
# create an instance of ApriltagDetectionsGetResponse from a dict
apriltag_detections_get_response_from_dict = ApriltagDetectionsGetResponse.from_dict(apriltag_detections_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


