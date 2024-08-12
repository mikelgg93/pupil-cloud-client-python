# BlinksTimeline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**has_blinks** | **int** |  | [optional] 
**max_blink_id** | **int** |  | [optional] 
**min_blink_id** | **int** |  | [optional] 
**start_timestamp** | **float** |  | [optional] 
**total_blinks_count** | **int** |  | [optional] 
**total_frames** | **int** |  | [optional] 
**unique_blinks_count** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.blinks_timeline import BlinksTimeline

# TODO update the JSON string below
json = "{}"
# create an instance of BlinksTimeline from a JSON string
blinks_timeline_instance = BlinksTimeline.from_json(json)
# print the JSON string representation of the object
print(BlinksTimeline.to_json())

# convert the object into a dict
blinks_timeline_dict = blinks_timeline_instance.to_dict()
# create an instance of BlinksTimeline from a dict
blinks_timeline_from_dict = BlinksTimeline.from_dict(blinks_timeline_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


