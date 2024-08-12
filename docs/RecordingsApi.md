# pupilcloud.RecordingsApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_recording_event**](RecordingsApi.md#create_recording_event) | **POST** /workspaces/{workspace_id}/recordings/{recording_id}/scene_camera.{format} | Create recording event
[**delete_recording**](RecordingsApi.md#delete_recording) | **DELETE** /workspaces/{workspace_id}/recordings/{recording_id} | Delete a recording
[**delete_recording_event_resource**](RecordingsApi.md#delete_recording_event_resource) | **DELETE** /workspaces/{workspace_id}/recordings/{recording_id}/events/{event_id} | Delete a recording event
[**delete_recordings**](RecordingsApi.md#delete_recordings) | **DELETE** /workspaces/{workspace_id}/recordings/ | Delete multiple recordings
[**download_raw_data_export_zip**](RecordingsApi.md#download_raw_data_export_zip) | **GET** /workspaces/{workspace_id}/recordings:raw-data-export | 
[**download_recording_file**](RecordingsApi.md#download_recording_file) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/files/{filename} | Download a recording&#39;s file
[**download_recording_zip**](RecordingsApi.md#download_recording_zip) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}.zip | Download recording files as a zip file
[**download_recordings_zip**](RecordingsApi.md#download_recordings_zip) | **GET** /workspaces/{workspace_id}/recordings.zip | Download multiple recordings in zip archive
[**get_apriltags_at_timestamp**](RecordingsApi.md#get_apriltags_at_timestamp) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/apriltags_at_timestamp/ | 
[**get_recording**](RecordingsApi.md#get_recording) | **GET** /workspaces/{workspace_id}/recordings/{recording_id} | Returns a recording with {recording_id}
[**get_recording_blinks**](RecordingsApi.md#get_recording_blinks) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/blinks.json | Recording blinks
[**get_recording_blinks_timeline**](RecordingsApi.md#get_recording_blinks_timeline) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/blinks_timeline | Recording blinks timeline
[**get_recording_events**](RecordingsApi.md#get_recording_events) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/events | List recording events
[**get_recording_face_detections**](RecordingsApi.md#get_recording_face_detections) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/face_detections | Recording face detections
[**get_recording_face_detections_timeline**](RecordingsApi.md#get_recording_face_detections_timeline) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/face_detections_timeline | Recording face detections
[**get_recording_files**](RecordingsApi.md#get_recording_files) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/files | List recording files
[**get_recording_fixations**](RecordingsApi.md#get_recording_fixations) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/fixations.json | Recording fixations
[**get_recording_fixations_timeline**](RecordingsApi.md#get_recording_fixations_timeline) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/fixations_timeline | Recording fixations timeline
[**get_recording_gaze**](RecordingsApi.md#get_recording_gaze) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/gaze.{format} | temporary endpoint for player development
[**get_recording_scanpath**](RecordingsApi.md#get_recording_scanpath) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/scanpath.{format} | Get list of fixation scanpath points per world frame
[**get_recording_scene_camera_intrinsics**](RecordingsApi.md#get_recording_scene_camera_intrinsics) | **GET** /workspaces/{workspace_id}/recordings/{recording_id}/scene_camera.{format} | Get Recording&#39;s Scene Camera Intrinsics
[**get_recordings**](RecordingsApi.md#get_recordings) | **GET** /workspaces/{workspace_id}/recordings/ | List all recordings
[**get_recordings_events_resource**](RecordingsApi.md#get_recordings_events_resource) | **GET** /workspaces/{workspace_id}/recordings:unique-events | 
[**patch_recording**](RecordingsApi.md#patch_recording) | **PATCH** /workspaces/{workspace_id}/recordings/{recording_id} | Update a recording
[**patch_recording_event_resource**](RecordingsApi.md#patch_recording_event_resource) | **PATCH** /workspaces/{workspace_id}/recordings/{recording_id}/events/{event_id} | Update a recording event
[**post_recording_event**](RecordingsApi.md#post_recording_event) | **POST** /workspaces/{workspace_id}/recordings/{recording_id}/events | Create a new recording event


# **create_recording_event**
> RecordingEventCreateResponse create_recording_event(workspace_id, recording_id, format, payload)

Create recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.create_recording_event import CreateRecordingEvent
from pupilcloud.models.recording_event_create_response import RecordingEventCreateResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    payload = pupilcloud.CreateRecordingEvent() # CreateRecordingEvent | 

    try:
        # Create recording event
        api_response = await api_instance.create_recording_event(workspace_id, recording_id, format, payload)
        print("The response of RecordingsApi->create_recording_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->create_recording_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **payload** | [**CreateRecordingEvent**](CreateRecordingEvent.md)|  | 

### Return type

[**RecordingEventCreateResponse**](RecordingEventCreateResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created recording event |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(workspace_id, recording_id)

Delete a recording

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # Delete a recording
        await api_instance.delete_recording(workspace_id, recording_id)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording_event_resource**
> RecordingEventResourceDeleteResponse delete_recording_event_resource(workspace_id, recording_id, event_id)

Delete a recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_event_resource_delete_response import RecordingEventResourceDeleteResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 

    try:
        # Delete a recording event
        api_response = await api_instance.delete_recording_event_resource(workspace_id, recording_id, event_id)
        print("The response of RecordingsApi->delete_recording_event_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 

### Return type

[**RecordingEventResourceDeleteResponse**](RecordingEventResourceDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted event |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recordings**
> delete_recordings(workspace_id, payload)

Delete multiple recordings

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recordings_delete_request import RecordingsDeleteRequest
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.RecordingsDeleteRequest() # RecordingsDeleteRequest | 

    try:
        # Delete multiple recordings
        await api_instance.delete_recordings(workspace_id, payload)
    except Exception as e:
        print("Exception when calling RecordingsApi->delete_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**RecordingsDeleteRequest**](RecordingsDeleteRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_raw_data_export_zip**
> bytearray download_raw_data_export_zip(workspace_id, ids=ids, exclude=exclude)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    ids = ['ids_example'] # List[str] | Recordings UUIDs for which data is to be exported (optional)
    exclude = ['exclude_example'] # List[str] | file to exclude (optional)

    try:
        api_response = await api_instance.download_raw_data_export_zip(workspace_id, ids=ids, exclude=exclude)
        print("The response of RecordingsApi->download_raw_data_export_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->download_raw_data_export_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **ids** | [**List[str]**](str.md)| Recordings UUIDs for which data is to be exported | [optional] 
 **exclude** | [**List[str]**](str.md)| file to exclude | [optional] 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording raw data export zip file archive |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recording_file**
> bytearray download_recording_file(workspace_id, recording_id, filename)

Download a recording's file

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    filename = 'filename_example' # str | 

    try:
        # Download a recording's file
        api_response = await api_instance.download_recording_file(workspace_id, recording_id, filename)
        print("The response of RecordingsApi->download_recording_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->download_recording_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **filename** | **str**|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**302** | Redirection url to download file |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recording_zip**
> bytearray download_recording_zip(workspace_id, recording_id)

Download recording files as a zip file

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # Download recording files as a zip file
        api_response = await api_instance.download_recording_zip(workspace_id, recording_id)
        print("The response of RecordingsApi->download_recording_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->download_recording_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording as a zip file archive |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recordings_zip**
> download_recordings_zip(workspace_id, ids=ids)

Download multiple recordings in zip archive

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    ids = ['ids_example'] # List[str] | recording ids to download (optional)

    try:
        # Download multiple recordings in zip archive
        await api_instance.download_recordings_zip(workspace_id, ids=ids)
    except Exception as e:
        print("Exception when calling RecordingsApi->download_recordings_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **ids** | [**List[str]**](str.md)| recording ids to download | [optional] 

### Return type

void (empty response body)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recordings as a zip file archive |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apriltags_at_timestamp**
> ApriltagsAtTimestampGetResponse get_apriltags_at_timestamp(workspace_id, recording_id, timestamp=timestamp, with_duplicates=with_duplicates)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.apriltags_at_timestamp_get_response import ApriltagsAtTimestampGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    timestamp = None # object | timestamp offset in recording in seconds (optional)
    with_duplicates = True # bool | return duplicate apriltags (defaults to best) (optional)

    try:
        api_response = await api_instance.get_apriltags_at_timestamp(workspace_id, recording_id, timestamp=timestamp, with_duplicates=with_duplicates)
        print("The response of RecordingsApi->get_apriltags_at_timestamp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_apriltags_at_timestamp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **timestamp** | [**object**](.md)| timestamp offset in recording in seconds | [optional] 
 **with_duplicates** | **bool**| return duplicate apriltags (defaults to best) | [optional] 

### Return type

[**ApriltagsAtTimestampGetResponse**](ApriltagsAtTimestampGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Apriltags in frame |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording**
> RecordingGetResponse get_recording(workspace_id, recording_id)

Returns a recording with {recording_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_get_response import RecordingGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # Returns a recording with {recording_id}
        api_response = await api_instance.get_recording(workspace_id, recording_id)
        print("The response of RecordingsApi->get_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

[**RecordingGetResponse**](RecordingGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single recording |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Recording doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_blinks**
> RecordingBlinksGetResponse get_recording_blinks(workspace_id, recording_id, start=start, end=end)

Recording blinks

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_blinks_get_response import RecordingBlinksGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)

    try:
        # Recording blinks
        api_response = await api_instance.get_recording_blinks(workspace_id, recording_id, start=start, end=end)
        print("The response of RecordingsApi->get_recording_blinks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_blinks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 

### Return type

[**RecordingBlinksGetResponse**](RecordingBlinksGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording blinks |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_blinks_timeline**
> RecordingBlinksTimelineGetResponse get_recording_blinks_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)

Recording blinks timeline

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_blinks_timeline_get_response import RecordingBlinksTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording blinks timeline
        api_response = await api_instance.get_recording_blinks_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)
        print("The response of RecordingsApi->get_recording_blinks_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_blinks_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**RecordingBlinksTimelineGetResponse**](RecordingBlinksTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of blinks |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_events**
> RecordingEventsGetResponse get_recording_events(workspace_id, recording_id)

List recording events

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_events_get_response import RecordingEventsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # List recording events
        api_response = await api_instance.get_recording_events(workspace_id, recording_id)
        print("The response of RecordingsApi->get_recording_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

[**RecordingEventsGetResponse**](RecordingEventsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recording events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_face_detections**
> RecordingFaceDetectionsGetResponse get_recording_face_detections(workspace_id, recording_id, start=start, end=end, with_landmarks=with_landmarks)

Recording face detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_face_detections_get_response import RecordingFaceDetectionsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    with_landmarks = True # bool |  (optional)

    try:
        # Recording face detections
        api_response = await api_instance.get_recording_face_detections(workspace_id, recording_id, start=start, end=end, with_landmarks=with_landmarks)
        print("The response of RecordingsApi->get_recording_face_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_face_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **with_landmarks** | **bool**|  | [optional] 

### Return type

[**RecordingFaceDetectionsGetResponse**](RecordingFaceDetectionsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of face detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_face_detections_timeline**
> RecordingFaceDetectionsTimelineGetResponse get_recording_face_detections_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)

Recording face detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_face_detections_timeline_get_response import RecordingFaceDetectionsTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording face detections
        api_response = await api_instance.get_recording_face_detections_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)
        print("The response of RecordingsApi->get_recording_face_detections_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_face_detections_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**RecordingFaceDetectionsTimelineGetResponse**](RecordingFaceDetectionsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of face detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_files**
> RecordingFilesGetResponse get_recording_files(workspace_id, recording_id)

List recording files

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_files_get_response import RecordingFilesGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 

    try:
        # List recording files
        api_response = await api_instance.get_recording_files(workspace_id, recording_id)
        print("The response of RecordingsApi->get_recording_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 

### Return type

[**RecordingFilesGetResponse**](RecordingFilesGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of a recording&#39;s files |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_fixations**
> RecordingFixationsGetResponse get_recording_fixations(workspace_id, recording_id, start=start, end=end, source=source)

Recording fixations

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_fixations_get_response import RecordingFixationsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    source = 'source_example' # str | source of the fixations (optional)

    try:
        # Recording fixations
        api_response = await api_instance.get_recording_fixations(workspace_id, recording_id, start=start, end=end, source=source)
        print("The response of RecordingsApi->get_recording_fixations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_fixations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **source** | **str**| source of the fixations | [optional] 

### Return type

[**RecordingFixationsGetResponse**](RecordingFixationsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording fixations |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_fixations_timeline**
> RecordingFixationsTimelineGetResponse get_recording_fixations_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)

Recording fixations timeline

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_fixations_timeline_get_response import RecordingFixationsTimelineGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording fixations timeline
        api_response = await api_instance.get_recording_fixations_timeline(workspace_id, recording_id, start=start, end=end, intervalsize=intervalsize)
        print("The response of RecordingsApi->get_recording_fixations_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_fixations_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**RecordingFixationsTimelineGetResponse**](RecordingFixationsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of fixations |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_gaze**
> RecordingGazeGetResponse get_recording_gaze(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)

temporary endpoint for player development

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_gaze_get_response import RecordingGazeGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    max_length = 3.4 # float |  (optional)

    try:
        # temporary endpoint for player development
        api_response = await api_instance.get_recording_gaze(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)
        print("The response of RecordingsApi->get_recording_gaze:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_gaze: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **max_length** | **float**|  | [optional] 

### Return type

[**RecordingGazeGetResponse**](RecordingGazeGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of gaze points |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_scanpath**
> RecordingScanpathGetResponse get_recording_scanpath(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)

Get list of fixation scanpath points per world frame

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_scanpath_get_response import RecordingScanpathGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    max_length = 3.4 # float |  (optional)

    try:
        # Get list of fixation scanpath points per world frame
        api_response = await api_instance.get_recording_scanpath(workspace_id, recording_id, format, start=start, end=end, max_length=max_length)
        print("The response of RecordingsApi->get_recording_scanpath:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_scanpath: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **max_length** | **float**|  | [optional] 

### Return type

[**RecordingScanpathGetResponse**](RecordingScanpathGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of fixation scanpath points |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_scene_camera_intrinsics**
> RecordingSceneCameraIntrinsicsGetResponse get_recording_scene_camera_intrinsics(workspace_id, recording_id, format)

Get Recording's Scene Camera Intrinsics

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_scene_camera_intrinsics_get_response import RecordingSceneCameraIntrinsicsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 

    try:
        # Get Recording's Scene Camera Intrinsics
        api_response = await api_instance.get_recording_scene_camera_intrinsics(workspace_id, recording_id, format)
        print("The response of RecordingsApi->get_recording_scene_camera_intrinsics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recording_scene_camera_intrinsics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **format** | **str**|  | 

### Return type

[**RecordingSceneCameraIntrinsicsGetResponse**](RecordingSceneCameraIntrinsicsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scene Camera Intrinsics of the specified recording |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings**
> RecordingsGetResponse get_recordings(workspace_id, trashed=trashed)

List all recordings

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recordings_get_response import RecordingsGetResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    trashed = False # bool |  (optional) (default to False)

    try:
        # List all recordings
        api_response = await api_instance.get_recordings(workspace_id, trashed=trashed)
        print("The response of RecordingsApi->get_recordings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recordings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **trashed** | **bool**|  | [optional] [default to False]

### Return type

[**RecordingsGetResponse**](RecordingsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recordings |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings_events_resource**
> get_recordings_events_resource(workspace_id)



### Example


```python
import pupilcloud
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)


# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        await api_instance.get_recordings_events_resource(workspace_id)
    except Exception as e:
        print("Exception when calling RecordingsApi->get_recordings_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recording**
> RecordingPatchResponse patch_recording(workspace_id, recording_id, payload)

Update a recording

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_patch_request import RecordingPatchRequest
from pupilcloud.models.recording_patch_response import RecordingPatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    payload = pupilcloud.RecordingPatchRequest() # RecordingPatchRequest | 

    try:
        # Update a recording
        api_response = await api_instance.patch_recording(workspace_id, recording_id, payload)
        print("The response of RecordingsApi->patch_recording:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->patch_recording: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **payload** | [**RecordingPatchRequest**](RecordingPatchRequest.md)|  | 

### Return type

[**RecordingPatchResponse**](RecordingPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated recording |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recording_event_resource**
> RecordingEventResourcePatchResponse patch_recording_event_resource(workspace_id, recording_id, event_id, payload)

Update a recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_event_patch_request import RecordingEventPatchRequest
from pupilcloud.models.recording_event_resource_patch_response import RecordingEventResourcePatchResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 
    payload = pupilcloud.RecordingEventPatchRequest() # RecordingEventPatchRequest | 

    try:
        # Update a recording event
        api_response = await api_instance.patch_recording_event_resource(workspace_id, recording_id, event_id, payload)
        print("The response of RecordingsApi->patch_recording_event_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->patch_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 
 **payload** | [**RecordingEventPatchRequest**](RecordingEventPatchRequest.md)|  | 

### Return type

[**RecordingEventResourcePatchResponse**](RecordingEventResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated event |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_recording_event**
> RecordingEventPostResponse post_recording_event(workspace_id, recording_id, payload)

Create a new recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.recording_event_post_request import RecordingEventPostRequest
from pupilcloud.models.recording_event_post_response import RecordingEventPostResponse
from pupilcloud.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.cloud.pupil-labs.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = pupilcloud.Configuration(
    host = "https://api.cloud.pupil-labs.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: workspace_id
configuration.api_key['workspace_id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['workspace_id'] = 'Bearer'

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
async with pupilcloud.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pupilcloud.RecordingsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    recording_id = 'recording_id_example' # str | 
    payload = pupilcloud.RecordingEventPostRequest() # RecordingEventPostRequest | 

    try:
        # Create a new recording event
        api_response = await api_instance.post_recording_event(workspace_id, recording_id, payload)
        print("The response of RecordingsApi->post_recording_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordingsApi->post_recording_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **recording_id** | **str**|  | 
 **payload** | [**RecordingEventPostRequest**](RecordingEventPostRequest.md)|  | 

### Return type

[**RecordingEventPostResponse**](RecordingEventPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created recording event |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

