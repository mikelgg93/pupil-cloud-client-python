# VisualizationConfigsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[VisualizationConfig]**](VisualizationConfig.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.visualization_configs_get_response import VisualizationConfigsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationConfigsGetResponse from a JSON string
visualization_configs_get_response_instance = VisualizationConfigsGetResponse.from_json(json)
# print the JSON string representation of the object
print(VisualizationConfigsGetResponse.to_json())

# convert the object into a dict
visualization_configs_get_response_dict = visualization_configs_get_response_instance.to_dict()
# create an instance of VisualizationConfigsGetResponse from a dict
visualization_configs_get_response_from_dict = VisualizationConfigsGetResponse.from_dict(visualization_configs_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


