# RecordingFilesGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[RecordingFile]**](RecordingFile.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_files_get_response import RecordingFilesGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFilesGetResponse from a JSON string
recording_files_get_response_instance = RecordingFilesGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingFilesGetResponse.to_json())

# convert the object into a dict
recording_files_get_response_dict = recording_files_get_response_instance.to_dict()
# create an instance of RecordingFilesGetResponse from a dict
recording_files_get_response_from_dict = RecordingFilesGetResponse.from_dict(recording_files_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


