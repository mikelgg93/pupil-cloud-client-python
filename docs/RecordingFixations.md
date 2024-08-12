# RecordingFixations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked_fixations** | **int** |  | [optional] 
**total_fixations** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.recording_fixations import RecordingFixations

# TODO update the JSON string below
json = "{}"
# create an instance of RecordingFixations from a JSON string
recording_fixations_instance = RecordingFixations.from_json(json)
# print the JSON string representation of the object
print(RecordingFixations.to_json())

# convert the object into a dict
recording_fixations_dict = recording_fixations_instance.to_dict()
# create an instance of RecordingFixations from a dict
recording_fixations_from_dict = RecordingFixations.from_dict(recording_fixations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


