# ProjectEnrichmentResourcePatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**ProjectEnrichment**](ProjectEnrichment.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_enrichment_resource_patch_response import ProjectEnrichmentResourcePatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEnrichmentResourcePatchResponse from a JSON string
project_enrichment_resource_patch_response_instance = ProjectEnrichmentResourcePatchResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectEnrichmentResourcePatchResponse.to_json())

# convert the object into a dict
project_enrichment_resource_patch_response_dict = project_enrichment_resource_patch_response_instance.to_dict()
# create an instance of ProjectEnrichmentResourcePatchResponse from a dict
project_enrichment_resource_patch_response_from_dict = ProjectEnrichmentResourcePatchResponse.from_dict(project_enrichment_resource_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


