# ProjectEnrichmentPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**from_event_name** | **str** |  | 
**id** | **str** |  | [optional] 
**kind** | **str** | the enrichment kind | [optional] 
**name** | **str** |  | 
**project_id** | **str** |  | [optional] 
**to_event_name** | **str** |  | 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.project_enrichment_post_request import ProjectEnrichmentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEnrichmentPostRequest from a JSON string
project_enrichment_post_request_instance = ProjectEnrichmentPostRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectEnrichmentPostRequest.to_json())

# convert the object into a dict
project_enrichment_post_request_dict = project_enrichment_post_request_instance.to_dict()
# create an instance of ProjectEnrichmentPostRequest from a dict
project_enrichment_post_request_from_dict = ProjectEnrichmentPostRequest.from_dict(project_enrichment_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


