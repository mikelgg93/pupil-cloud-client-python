# StaticImageMapperEnrichmentsRecordingFixationsGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**RecordingFixations**](RecordingFixations.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_enrichments_recording_fixations_get_response import StaticImageMapperEnrichmentsRecordingFixationsGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperEnrichmentsRecordingFixationsGetResponse from a JSON string
static_image_mapper_enrichments_recording_fixations_get_response_instance = StaticImageMapperEnrichmentsRecordingFixationsGetResponse.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperEnrichmentsRecordingFixationsGetResponse.to_json())

# convert the object into a dict
static_image_mapper_enrichments_recording_fixations_get_response_dict = static_image_mapper_enrichments_recording_fixations_get_response_instance.to_dict()
# create an instance of StaticImageMapperEnrichmentsRecordingFixationsGetResponse from a dict
static_image_mapper_enrichments_recording_fixations_get_response_from_dict = StaticImageMapperEnrichmentsRecordingFixationsGetResponse.from_dict(static_image_mapper_enrichments_recording_fixations_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


