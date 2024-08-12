# StaticImageMapperEnrichmentPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**StaticImageMapperGetRequest**](StaticImageMapperGetRequest.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_enrichment_patch_response import StaticImageMapperEnrichmentPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperEnrichmentPatchResponse from a JSON string
static_image_mapper_enrichment_patch_response_instance = StaticImageMapperEnrichmentPatchResponse.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperEnrichmentPatchResponse.to_json())

# convert the object into a dict
static_image_mapper_enrichment_patch_response_dict = static_image_mapper_enrichment_patch_response_instance.to_dict()
# create an instance of StaticImageMapperEnrichmentPatchResponse from a dict
static_image_mapper_enrichment_patch_response_from_dict = StaticImageMapperEnrichmentPatchResponse.from_dict(static_image_mapper_enrichment_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


