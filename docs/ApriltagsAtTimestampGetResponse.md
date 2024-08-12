# ApriltagsAtTimestampGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Tags**](Tags.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.apriltags_at_timestamp_get_response import ApriltagsAtTimestampGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApriltagsAtTimestampGetResponse from a JSON string
apriltags_at_timestamp_get_response_instance = ApriltagsAtTimestampGetResponse.from_json(json)
# print the JSON string representation of the object
print(ApriltagsAtTimestampGetResponse.to_json())

# convert the object into a dict
apriltags_at_timestamp_get_response_dict = apriltags_at_timestamp_get_response_instance.to_dict()
# create an instance of ApriltagsAtTimestampGetResponse from a dict
apriltags_at_timestamp_get_response_from_dict = ApriltagsAtTimestampGetResponse.from_dict(apriltags_at_timestamp_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


