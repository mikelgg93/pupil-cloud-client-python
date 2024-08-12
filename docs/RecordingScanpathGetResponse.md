# RecordingScanpathGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Scanpath]**](Scanpath.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_scanpath_get_response import RecordingScanpathGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingScanpathGetResponse from a JSON string
recording_scanpath_get_response_instance = RecordingScanpathGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingScanpathGetResponse.to_json())

# convert the object into a dict
recording_scanpath_get_response_dict = recording_scanpath_get_response_instance.to_dict()
# create an instance of RecordingScanpathGetResponse from a dict
recording_scanpath_get_response_from_dict = RecordingScanpathGetResponse.from_dict(recording_scanpath_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


