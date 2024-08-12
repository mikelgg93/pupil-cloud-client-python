# VisualizationConfigPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**enrichment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** | The type of visualization | 
**name** | **str** |  | 
**payload** | **Dict[str, object]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.visualization_config_post_request import VisualizationConfigPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationConfigPostRequest from a JSON string
visualization_config_post_request_instance = VisualizationConfigPostRequest.from_json(json)
# print the JSON string representation of the object
print(VisualizationConfigPostRequest.to_json())

# convert the object into a dict
visualization_config_post_request_dict = visualization_config_post_request_instance.to_dict()
# create an instance of VisualizationConfigPostRequest from a dict
visualization_config_post_request_from_dict = VisualizationConfigPostRequest.from_dict(visualization_config_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


