# Markerless


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**reference_image_id** | **str** |  | [optional] 
**reference_image_thumbnail_url** | **str** |  | [optional] 
**scanning_recording_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.markerless import Markerless

# TODO update the JSON string below
json = "{}"
# create an instance of Markerless from a JSON string
markerless_instance = Markerless.from_json(json)
# print the JSON string representation of the object
print(Markerless.to_json())

# convert the object into a dict
markerless_dict = markerless_instance.to_dict()
# create an instance of Markerless from a dict
markerless_from_dict = Markerless.from_dict(markerless_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


