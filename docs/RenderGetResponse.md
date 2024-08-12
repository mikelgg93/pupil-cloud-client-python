# RenderGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorldRender**](WorldRender.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.render_get_response import RenderGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenderGetResponse from a JSON string
render_get_response_instance = RenderGetResponse.from_json(json)
# print the JSON string representation of the object
print(RenderGetResponse.to_json())

# convert the object into a dict
render_get_response_dict = render_get_response_instance.to_dict()
# create an instance of RenderGetResponse from a dict
render_get_response_from_dict = RenderGetResponse.from_dict(render_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


