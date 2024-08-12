# VisualizationConfigGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**VisualizationConfig**](VisualizationConfig.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.visualization_config_get_response import VisualizationConfigGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationConfigGetResponse from a JSON string
visualization_config_get_response_instance = VisualizationConfigGetResponse.from_json(json)
# print the JSON string representation of the object
print(VisualizationConfigGetResponse.to_json())

# convert the object into a dict
visualization_config_get_response_dict = visualization_config_get_response_instance.to_dict()
# create an instance of VisualizationConfigGetResponse from a dict
visualization_config_get_response_from_dict = VisualizationConfigGetResponse.from_dict(visualization_config_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


