# LabelPatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**LabelsResponse**](LabelsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.label_patch_response import LabelPatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPatchResponse from a JSON string
label_patch_response_instance = LabelPatchResponse.from_json(json)
# print the JSON string representation of the object
print(LabelPatchResponse.to_json())

# convert the object into a dict
label_patch_response_dict = label_patch_response_instance.to_dict()
# create an instance of LabelPatchResponse from a dict
label_patch_response_from_dict = LabelPatchResponse.from_dict(label_patch_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


