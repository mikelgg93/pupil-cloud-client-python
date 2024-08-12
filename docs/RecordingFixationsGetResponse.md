# RecordingFixationsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Fixations]**](Fixations.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_fixations_get_response import RecordingFixationsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFixationsGetResponse from a JSON string
recording_fixations_get_response_instance = RecordingFixationsGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingFixationsGetResponse.to_json())

# convert the object into a dict
recording_fixations_get_response_dict = recording_fixations_get_response_instance.to_dict()
# create an instance of RecordingFixationsGetResponse from a dict
recording_fixations_get_response_from_dict = RecordingFixationsGetResponse.from_dict(recording_fixations_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


