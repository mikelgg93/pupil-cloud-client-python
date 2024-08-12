# StaticImageMapperPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**from_event_name** | **str** |  | 
**name** | **str** |  | 
**static_image_id** | **str** |  | [optional] 
**to_event_name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_post_request import StaticImageMapperPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperPostRequest from a JSON string
static_image_mapper_post_request_instance = StaticImageMapperPostRequest.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperPostRequest.to_json())

# convert the object into a dict
static_image_mapper_post_request_dict = static_image_mapper_post_request_instance.to_dict()
# create an instance of StaticImageMapperPostRequest from a dict
static_image_mapper_post_request_from_dict = StaticImageMapperPostRequest.from_dict(static_image_mapper_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


