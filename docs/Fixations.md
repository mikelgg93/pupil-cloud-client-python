# Fixations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start** | **float** |  | [optional] 
**stop** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.fixations import Fixations

# TODO update the JSON string below
json = "{}"
# create an instance of Fixations from a JSON string
fixations_instance = Fixations.from_json(json)
# print the JSON string representation of the object
print(Fixations.to_json())

# convert the object into a dict
fixations_dict = fixations_instance.to_dict()
# create an instance of Fixations from a dict
fixations_from_dict = Fixations.from_dict(fixations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


