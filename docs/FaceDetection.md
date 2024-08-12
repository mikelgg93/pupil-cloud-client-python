# FaceDetection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_timestamp** | **float** |  | [optional] 
**faces** | [**List[Face]**](Face.md) |  | [optional] 
**start_timestamp** | **float** |  | [optional] 

## Example

```python
from pupilcloud.models.face_detection import FaceDetection

# TODO update the JSON string below
json = "{}"
# create an instance of FaceDetection from a JSON string
face_detection_instance = FaceDetection.from_json(json)
# print the JSON string representation of the object
print(FaceDetection.to_json())

# convert the object into a dict
face_detection_dict = face_detection_instance.to_dict()
# create an instance of FaceDetection from a dict
face_detection_from_dict = FaceDetection.from_dict(face_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


