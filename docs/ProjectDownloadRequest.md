# ProjectDownloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrichments** | [**List[EnrichmentDownloadSpec]**](EnrichmentDownloadSpec.md) |  | [optional] 
**recordings** | [**List[RecordingDownloadSpec]**](RecordingDownloadSpec.md) |  | [optional] 

## Example

```python
from pupilcloud.models.project_download_request import ProjectDownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDownloadRequest from a JSON string
project_download_request_instance = ProjectDownloadRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectDownloadRequest.to_json())

# convert the object into a dict
project_download_request_dict = project_download_request_instance.to_dict()
# create an instance of ProjectDownloadRequest from a dict
project_download_request_from_dict = ProjectDownloadRequest.from_dict(project_download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


