# RecordingsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[Recording]**](Recording.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.recordings_get_response import RecordingsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingsGetResponse from a JSON string
recordings_get_response_instance = RecordingsGetResponse.from_json(json)
# print the JSON string representation of the object
print(RecordingsGetResponse.to_json())

# convert the object into a dict
recordings_get_response_dict = recordings_get_response_instance.to_dict()
# create an instance of RecordingsGetResponse from a dict
recordings_get_response_from_dict = RecordingsGetResponse.from_dict(recordings_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


