# LabelPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aoi_ids** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**recording_ids** | **List[str]** |  | [optional] 
**template_ids** | **List[str]** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from pupilcloud.models.label_post_request import LabelPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPostRequest from a JSON string
label_post_request_instance = LabelPostRequest.from_json(json)
# print the JSON string representation of the object
print(LabelPostRequest.to_json())

# convert the object into a dict
label_post_request_dict = label_post_request_instance.to_dict()
# create an instance of LabelPostRequest from a dict
label_post_request_from_dict = LabelPostRequest.from_dict(label_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


