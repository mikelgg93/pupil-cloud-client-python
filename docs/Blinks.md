# Blinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**start** | **float** |  | [optional] 
**stop** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.blinks import Blinks

# TODO update the JSON string below
json = "{}"
# create an instance of Blinks from a JSON string
blinks_instance = Blinks.from_json(json)
# print the JSON string representation of the object
print(Blinks.to_json())

# convert the object into a dict
blinks_dict = blinks_instance.to_dict()
# create an instance of Blinks from a dict
blinks_from_dict = Blinks.from_dict(blinks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


