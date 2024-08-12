# MarkerlessInitialization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_image_id** | **str** |  | 
**scanning_recording_id** | **str** |  | 

## Example

```python
from pupilcloud.models.markerless_initialization import MarkerlessInitialization

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessInitialization from a JSON string
markerless_initialization_instance = MarkerlessInitialization.from_json(json)
# print the JSON string representation of the object
print(MarkerlessInitialization.to_json())

# convert the object into a dict
markerless_initialization_dict = markerless_initialization_instance.to_dict()
# create an instance of MarkerlessInitialization from a dict
markerless_initialization_from_dict = MarkerlessInitialization.from_dict(markerless_initialization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


