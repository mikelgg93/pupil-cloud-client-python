# InitializeRenderingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorldRender**](WorldRender.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.initialize_rendering_response import InitializeRenderingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeRenderingResponse from a JSON string
initialize_rendering_response_instance = InitializeRenderingResponse.from_json(json)
# print the JSON string representation of the object
print(InitializeRenderingResponse.to_json())

# convert the object into a dict
initialize_rendering_response_dict = initialize_rendering_response_instance.to_dict()
# create an instance of InitializeRenderingResponse from a dict
initialize_rendering_response_from_dict = InitializeRenderingResponse.from_dict(initialize_rendering_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


