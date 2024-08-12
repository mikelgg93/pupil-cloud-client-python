# StaticImageMapperEnrichmentGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**StaticImageMapperGetRequest**](StaticImageMapperGetRequest.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_enrichment_get_response import StaticImageMapperEnrichmentGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperEnrichmentGetResponse from a JSON string
static_image_mapper_enrichment_get_response_instance = StaticImageMapperEnrichmentGetResponse.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperEnrichmentGetResponse.to_json())

# convert the object into a dict
static_image_mapper_enrichment_get_response_dict = static_image_mapper_enrichment_get_response_instance.to_dict()
# create an instance of StaticImageMapperEnrichmentGetResponse from a dict
static_image_mapper_enrichment_get_response_from_dict = StaticImageMapperEnrichmentGetResponse.from_dict(static_image_mapper_enrichment_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


