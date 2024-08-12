# StaticImageMapperEnrichmentsRecordingFixationPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **float** |  | [optional] 
**result** | [**FixationDatapoint**](FixationDatapoint.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from pupilcloud.models.static_image_mapper_enrichments_recording_fixation_put_response import StaticImageMapperEnrichmentsRecordingFixationPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticImageMapperEnrichmentsRecordingFixationPutResponse from a JSON string
static_image_mapper_enrichments_recording_fixation_put_response_instance = StaticImageMapperEnrichmentsRecordingFixationPutResponse.from_json(json)
# print the JSON string representation of the object
print(StaticImageMapperEnrichmentsRecordingFixationPutResponse.to_json())

# convert the object into a dict
static_image_mapper_enrichments_recording_fixation_put_response_dict = static_image_mapper_enrichments_recording_fixation_put_response_instance.to_dict()
# create an instance of StaticImageMapperEnrichmentsRecordingFixationPutResponse from a dict
static_image_mapper_enrichments_recording_fixation_put_response_from_dict = StaticImageMapperEnrichmentsRecordingFixationPutResponse.from_dict(static_image_mapper_enrichments_recording_fixation_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


