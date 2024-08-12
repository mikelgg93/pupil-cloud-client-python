# ProjectEnrichmentsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[ProjectEnrichment]**](ProjectEnrichment.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.project_enrichments_get_response import ProjectEnrichmentsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectEnrichmentsGetResponse from a JSON string
project_enrichments_get_response_instance = ProjectEnrichmentsGetResponse.from_json(json)
# print the JSON string representation of the object
print(ProjectEnrichmentsGetResponse.to_json())

# convert the object into a dict
project_enrichments_get_response_dict = project_enrichments_get_response_instance.to_dict()
# create an instance of ProjectEnrichmentsGetResponse from a dict
project_enrichments_get_response_from_dict = ProjectEnrichmentsGetResponse.from_dict(project_enrichments_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


