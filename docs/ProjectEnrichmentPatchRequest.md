# ProjectEnrichmentPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**from_event_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** | the enrichment kind | [optional] 
**name** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**to_event_name** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.project_enrichment_patch_request import ProjectEnrichmentPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEnrichmentPatchRequest from a JSON string
project_enrichment_patch_request_instance = ProjectEnrichmentPatchRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectEnrichmentPatchRequest.to_json())

# convert the object into a dict
project_enrichment_patch_request_dict = project_enrichment_patch_request_instance.to_dict()
# create an instance of ProjectEnrichmentPatchRequest from a dict
project_enrichment_patch_request_from_dict = ProjectEnrichmentPatchRequest.from_dict(project_enrichment_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


