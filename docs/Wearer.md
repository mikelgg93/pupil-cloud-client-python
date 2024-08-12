# Wearer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived_at** | **datetime** |  | [optional] 
**archived_by_user_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by_user_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ied** | **float** |  | [optional] 
**name** | **str** |  | 
**offset_correction** | [**OffsetCorrection**](OffsetCorrection.md) |  | [optional] 
**training_updated_on** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**workspace_id** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.wearer import Wearer

# TODO update the JSON string below
json = "{}"
# create an instance of Wearer from a JSON string
wearer_instance = Wearer.from_json(json)
# print the JSON string representation of the object
print(Wearer.to_json())

# convert the object into a dict
wearer_dict = wearer_instance.to_dict()
# create an instance of Wearer from a dict
wearer_from_dict = Wearer.from_dict(wearer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


