# FixationDatapoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**fixation_id** | **int** |  | [optional] 
**seek_timestamp** | **float** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.fixation_datapoint import FixationDatapoint

# TODO update the JSON string below
json = "{}"
# create an instance of FixationDatapoint from a JSON string
fixation_datapoint_instance = FixationDatapoint.from_json(json)
# print the JSON string representation of the object
print(FixationDatapoint.to_json())

# convert the object into a dict
fixation_datapoint_dict = fixation_datapoint_instance.to_dict()
# create an instance of FixationDatapoint from a dict
fixation_datapoint_from_dict = FixationDatapoint.from_dict(fixation_datapoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


