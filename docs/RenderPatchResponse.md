# RenderPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**WorldRender**](WorldRender.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.render_patch_response import RenderPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RenderPatchResponse from a JSON string
render_patch_response_instance = RenderPatchResponse.from_json(json)
# print the JSON string representation of the object
print(RenderPatchResponse.to_json())

# convert the object into a dict
render_patch_response_dict = render_patch_response_instance.to_dict()
# create an instance of RenderPatchResponse from a dict
render_patch_response_from_dict = RenderPatchResponse.from_dict(render_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


