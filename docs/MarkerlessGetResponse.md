# MarkerlessGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**Markerless**](Markerless.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.markerless_get_response import MarkerlessGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarkerlessGetResponse from a JSON string
markerless_get_response_instance = MarkerlessGetResponse.from_json(json)
# print the JSON string representation of the object
print(MarkerlessGetResponse.to_json())

# convert the object into a dict
markerless_get_response_dict = markerless_get_response_instance.to_dict()
# create an instance of MarkerlessGetResponse from a dict
markerless_get_response_from_dict = MarkerlessGetResponse.from_dict(markerless_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


