# LabelsDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_ids** | **List[str]** |  | [optional] 

## Example

```python
from pupilcloud.models.labels_delete_request import LabelsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelsDeleteRequest from a JSON string
labels_delete_request_instance = LabelsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(LabelsDeleteRequest.to_json())

# convert the object into a dict
labels_delete_request_dict = labels_delete_request_instance.to_dict()
# create an instance of LabelsDeleteRequest from a dict
labels_delete_request_from_dict = LabelsDeleteRequest.from_dict(labels_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


