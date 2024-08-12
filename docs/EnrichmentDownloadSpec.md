# EnrichmentDownloadSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrichment_id** | **str** |  | 
**exclude_files** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.enrichment_download_spec import EnrichmentDownloadSpec

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentDownloadSpec from a JSON string
enrichment_download_spec_instance = EnrichmentDownloadSpec.from_json(json)
# print the JSON string representation of the object
print(EnrichmentDownloadSpec.to_json())

# convert the object into a dict
enrichment_download_spec_dict = enrichment_download_spec_instance.to_dict()
# create an instance of EnrichmentDownloadSpec from a dict
enrichment_download_spec_from_dict = EnrichmentDownloadSpec.from_dict(enrichment_download_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


