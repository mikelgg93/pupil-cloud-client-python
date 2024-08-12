# InitializeMarkerlessResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Markerless**](Markerless.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.initialize_markerless_response import InitializeMarkerlessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeMarkerlessResponse from a JSON string
initialize_markerless_response_instance = InitializeMarkerlessResponse.from_json(json)
# print the JSON string representation of the object
print(InitializeMarkerlessResponse.to_json())

# convert the object into a dict
initialize_markerless_response_dict = initialize_markerless_response_instance.to_dict()
# create an instance of InitializeMarkerlessResponse from a dict
initialize_markerless_response_from_dict = InitializeMarkerlessResponse.from_dict(initialize_markerless_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


