# RecordingDownloadSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_files** | **List[str]** |  | [optional] 
**recording_id** | **str** |  | 

## Example

```python
from pupilcloud.models.recording_download_spec import RecordingDownloadSpec

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingDownloadSpec from a JSON string
recording_download_spec_instance = RecordingDownloadSpec.from_json(json)
# print the JSON string representation of the object
print(RecordingDownloadSpec.to_json())

# convert the object into a dict
recording_download_spec_dict = recording_download_spec_instance.to_dict()
# create an instance of RecordingDownloadSpec from a dict
recording_download_spec_from_dict = RecordingDownloadSpec.from_dict(recording_download_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


