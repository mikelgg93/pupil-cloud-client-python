# ProjectEnrichmentGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**ProjectEnrichment**](ProjectEnrichment.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_enrichment_get_response import ProjectEnrichmentGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEnrichmentGetResponse from a JSON string
project_enrichment_get_response_instance = ProjectEnrichmentGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectEnrichmentGetResponse.to_json())

# convert the object into a dict
project_enrichment_get_response_dict = project_enrichment_get_response_instance.to_dict()
# create an instance of ProjectEnrichmentGetResponse from a dict
project_enrichment_get_response_from_dict = ProjectEnrichmentGetResponse.from_dict(project_enrichment_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


