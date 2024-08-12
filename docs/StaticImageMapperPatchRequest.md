# StaticImageMapperPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_event_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**static_image_id** | **str** |  | [optional] 
**to_event_name** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_patch_request import StaticImageMapperPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperPatchRequest from a JSON string
static_image_mapper_patch_request_instance = StaticImageMapperPatchRequest.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperPatchRequest.to_json())

# convert the object into a dict
static_image_mapper_patch_request_dict = static_image_mapper_patch_request_instance.to_dict()
# create an instance of StaticImageMapperPatchRequest from a dict
static_image_mapper_patch_request_from_dict = StaticImageMapperPatchRequest.from_dict(static_image_mapper_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


