# StaticImageMapperEnrichmentPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**StaticImageMapperGetRequest**](StaticImageMapperGetRequest.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_enrichment_post_response import StaticImageMapperEnrichmentPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperEnrichmentPostResponse from a JSON string
static_image_mapper_enrichment_post_response_instance = StaticImageMapperEnrichmentPostResponse.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperEnrichmentPostResponse.to_json())

# convert the object into a dict
static_image_mapper_enrichment_post_response_dict = static_image_mapper_enrichment_post_response_instance.to_dict()
# create an instance of StaticImageMapperEnrichmentPostResponse from a dict
static_image_mapper_enrichment_post_response_from_dict = StaticImageMapperEnrichmentPostResponse.from_dict(static_image_mapper_enrichment_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


