# StaticImageMapperGetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**deleted_by_user_id** | **str** |  | [optional] 
**error_message** | **str** | static enrichment error message | [optional] 
**fixations_status** | [**List[FixationStatus]**](FixationStatus.md) |  | [optional] 
**from_event_name** | **str** |  | 
**id** | **str** |  | [optional] 
**kind** | **str** | the enrichment kind | [optional] 
**name** | **str** |  | 
**project_id** | **str** |  | [optional] 
**slices** | [**List[EnrichmentSlice]**](EnrichmentSlice.md) |  | [optional] 
**static_image_id** | **str** |  | [optional] 
**static_image_image_thumbnail_url** | **str** |  | [optional] 
**status** | [**EnrichmentStatus**](EnrichmentStatus.md) |  | [optional] 
**to_event_name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_get_request import StaticImageMapperGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperGetRequest from a JSON string
static_image_mapper_get_request_instance = StaticImageMapperGetRequest.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperGetRequest.to_json())

# convert the object into a dict
static_image_mapper_get_request_dict = static_image_mapper_get_request_instance.to_dict()
# create an instance of StaticImageMapperGetRequest from a dict
static_image_mapper_get_request_from_dict = StaticImageMapperGetRequest.from_dict(static_image_mapper_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


