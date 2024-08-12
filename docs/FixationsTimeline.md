# FixationsTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**has_fixations** | **int** |  | [optional] 
**max_fixation_id** | **int** |  | [optional] 
**min_fixation_id** | **int** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**total_fixations_count** | **int** |  | [optional] 
**total_frames** | **int** |  | [optional] 
**unique_fixations_count** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.fixations_timeline import FixationsTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of FixationsTimeline from a JSON string
fixations_timeline_instance = FixationsTimeline.from_json(json)
# print the JSON string representation of the object
print(FixationsTimeline.to_json())

# convert the object into a dict
fixations_timeline_dict = fixations_timeline_instance.to_dict()
# create an instance of FixationsTimeline from a dict
fixations_timeline_from_dict = FixationsTimeline.from_dict(fixations_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


