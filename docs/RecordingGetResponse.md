# RecordingGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**RecordingWithFilesResponse**](RecordingWithFilesResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_get_response import RecordingGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingGetResponse from a JSON string
recording_get_response_instance = RecordingGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingGetResponse.to_json())

# convert the object into a dict
recording_get_response_dict = recording_get_response_instance.to_dict()
# create an instance of RecordingGetResponse from a dict
recording_get_response_from_dict = RecordingGetResponse.from_dict(recording_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


