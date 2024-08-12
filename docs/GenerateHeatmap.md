# GenerateHeatmap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**colormap** | **str** | colormap for heatmap | [optional] [default to 'Turbo']
**enrichment_id** | **str** |  | 
**height** | **int** |  | [optional] 
**var_json** | **bool** |  | [optional] [default to False]
**max_size** | **int** |  | [optional] 
**n_bins** | **int** |  | [optional] 
**project_id** | **str** |  | 
**recording_ids** | **List[str]** |  | [optional] 
**sigma** | **float** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from pupilcloud.models.generate_heatmap import GenerateHeatmap

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateHeatmap from a JSON string
generate_heatmap_instance = GenerateHeatmap.from_json(json)
# print the JSON string representation of the object
print(GenerateHeatmap.to_json())

# convert the object into a dict
generate_heatmap_dict = generate_heatmap_instance.to_dict()
# create an instance of GenerateHeatmap from a dict
generate_heatmap_from_dict = GenerateHeatmap.from_dict(generate_heatmap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


