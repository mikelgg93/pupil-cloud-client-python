# LabelGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**LabelsResponse**](LabelsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.label_get_response import LabelGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelGetResponse from a JSON string
label_get_response_instance = LabelGetResponse.from_json(json)
# print the JSON string representation of the object
print(LabelGetResponse.to_json())

# convert the object into a dict
label_get_response_dict = label_get_response_instance.to_dict()
# create an instance of LabelGetResponse from a dict
label_get_response_from_dict = LabelGetResponse.from_dict(label_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


