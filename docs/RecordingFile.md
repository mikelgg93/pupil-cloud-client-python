# RecordingFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**mimetype** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size_bytes** | **int** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**uploaded_bytes** | **int** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_file import RecordingFile

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFile from a JSON string
recording_file_instance = RecordingFile.from_json(json)
# print the JSON string representation of the object
print(RecordingFile.to_json())

# convert the object into a dict
recording_file_dict = recording_file_instance.to_dict()
# create an instance of RecordingFile from a dict
recording_file_from_dict = RecordingFile.from_dict(recording_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


