# LabelsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**List[LabelsResponse]**](LabelsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.labels_get_response import LabelsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsGetResponse from a JSON string
labels_get_response_instance = LabelsGetResponse.from_json(json)
# print the JSON string representation of the object
print(LabelsGetResponse.to_json())

# convert the object into a dict
labels_get_response_dict = labels_get_response_instance.to_dict()
# create an instance of LabelsGetResponse from a dict
labels_get_response_from_dict = LabelsGetResponse.from_dict(labels_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


