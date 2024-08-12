# LabelPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**LabelsResponse**](LabelsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.label_post_response import LabelPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPostResponse from a JSON string
label_post_response_instance = LabelPostResponse.from_json(json)
# print the JSON string representation of the object
print(LabelPostResponse.to_json())

# convert the object into a dict
label_post_response_dict = label_post_response_instance.to_dict()
# create an instance of LabelPostResponse from a dict
label_post_response_from_dict = LabelPostResponse.from_dict(label_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


