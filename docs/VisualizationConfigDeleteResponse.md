# VisualizationConfigDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**VisualizationConfig**](VisualizationConfig.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.visualization_config_delete_response import VisualizationConfigDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationConfigDeleteResponse from a JSON string
visualization_config_delete_response_instance = VisualizationConfigDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(VisualizationConfigDeleteResponse.to_json())

# convert the object into a dict
visualization_config_delete_response_dict = visualization_config_delete_response_instance.to_dict()
# create an instance of VisualizationConfigDeleteResponse from a dict
visualization_config_delete_response_from_dict = VisualizationConfigDeleteResponse.from_dict(visualization_config_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


