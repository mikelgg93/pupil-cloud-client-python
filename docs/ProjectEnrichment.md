# ProjectEnrichment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_user_id** | **str** |  | [optional] 
**deleted_by_user_id** | **str** |  | [optional] 
**enrichment_id** | **str** |  | 
**fps** | **int** |  | [optional] 
**project_id** | **str** |  | 

## Example

```python
from pupilcloud.models.project_enrichment import ProjectEnrichment

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEnrichment from a JSON string
project_enrichment_instance = ProjectEnrichment.from_json(json)
# print the JSON string representation of the object
print(ProjectEnrichment.to_json())

# convert the object into a dict
project_enrichment_dict = project_enrichment_instance.to_dict()
# create an instance of ProjectEnrichment from a dict
project_enrichment_from_dict = ProjectEnrichment.from_dict(project_enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


