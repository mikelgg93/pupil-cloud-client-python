# pupilcloud.RecordingsApi

All URIs are relative to *https://api.cloud.pupil-labs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_recording**](RecordingsApi.md#delete_recording) | **DELETE** /recordings/{recording_id} | Delete a recording
[**download_recording_file**](RecordingsApi.md#download_recording_file) | **GET** /recordings/{recording_id}/files/{filename} | Download a recording&#39;s file
[**download_recording_zip**](RecordingsApi.md#download_recording_zip) | **GET** /recordings/{recording_id}.zip | Download recording files as a zip file
[**download_recordings_zip**](RecordingsApi.md#download_recordings_zip) | **GET** /recordings.zip | Download multiple recordings in zip archive
[**get_recording**](RecordingsApi.md#get_recording) | **GET** /recordings/{recording_id} | Returns a recording with {recording_id}
[**get_recording_events**](RecordingsApi.md#get_recording_events) | **GET** /recordings/{recording_id}/events | List recording events
[**get_recording_files**](RecordingsApi.md#get_recording_files) | **GET** /recordings/{recording_id}/files | List recording files
[**get_recordings**](RecordingsApi.md#get_recordings) | **GET** /recordings/ | List all recordings
[**patch_recording**](RecordingsApi.md#patch_recording) | **PATCH** /recordings/{recording_id} | Update a recording


# **delete_recording**
> delete_recording(recording_id)

Delete a recording

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
recording_id = 'recording_id_example' # str | 

try:
    # Delete a recording
    api.delete_recording(recording_id)
except ApiException as e:
    print("Exception when calling RecordingsApi->delete_recording: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Authentication is required |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recording_file**
> file download_recording_file(recording_id, filename)

Download a recording's file

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com", downloads_path="./downloads")
recording_id = 'recording_id_example' # str | 
filename = 'filename_example' # str | 

# Download a recording's file to disk
try:
    saved_path = api.download_recording_file(recording_id, filename)
    print("Saved to: %s" % saved_path)
except ApiException as e:
    print("Exception when calling RecordingsApi->download_recording_file: %s\n" % e)

# Download a recording's file in memory
try:
    response = api.download_recording_file(recording_id, filename, _preload_content=False)
    print("Data: %r" % response.read())
except ApiException as e:
    print("Exception when calling RecordingsApi->download_recording_file: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 
 **filename** | **str**|  | 

### Return type

**file**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**302** | Redirection url to download file |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recording_zip**
> file download_recording_zip(recording_id)

Download recording files as a zip file

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com", downloads_path="./downloads")
recording_id = 'recording_id_example' # str | 

# Download recording files as a zip file to disk
try:
    saved_path = api.download_recording_zip(recording_id)
    print("Saved to: %s" % saved_path)
except ApiException as e:
    print("Exception when calling RecordingsApi->download_recording_zip: %s\n" % e)

# Download recording files as a zip file in memory
try:
    response = api.download_recording_zip(recording_id, _preload_content=False)
    print("Data: %r" % response.read())
except ApiException as e:
    print("Exception when calling RecordingsApi->download_recording_zip: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

**file**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recording as a zip file archive |  -  |
**401** | Authentication is required |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_recordings_zip**
> download_recordings_zip(ids=ids)

Download multiple recordings in zip archive

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
ids = ['ids_example'] # list[str] | recording ids to download (optional)

try:
    # Download multiple recordings in zip archive
    api.download_recordings_zip(ids=ids)
except ApiException as e:
    print("Exception when calling RecordingsApi->download_recordings_zip: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| recording ids to download | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recordings as a zip file archive |  -  |
**401** | Authentication is required |  -  |
**503** | Recording still uploading |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording**
> RecordingGetResponse get_recording(recording_id)

Returns a recording with {recording_id}

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
recording_id = 'recording_id_example' # str | 

try:
    # Returns a recording with {recording_id}
    data = api.get_recording(recording_id).result
    print(data)
except ApiException as e:
    print("Exception when calling RecordingsApi->get_recording: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

[**RecordingGetResponse**](RecordingGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single recording |  -  |
**401** | Authentication is required |  -  |
**404** | Recording doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_events**
> RecordingEventsGetResponse get_recording_events(recording_id)

List recording events

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
recording_id = 'recording_id_example' # str | 

try:
    # List recording events
    data = api.get_recording_events(recording_id).result
    print(data)
except ApiException as e:
    print("Exception when calling RecordingsApi->get_recording_events: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

[**RecordingEventsGetResponse**](RecordingEventsGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recording events |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_files**
> RecordingFilesGetResponse get_recording_files(recording_id)

List recording files

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
recording_id = 'recording_id_example' # str | 

try:
    # List recording files
    data = api.get_recording_files(recording_id).result
    print(data)
except ApiException as e:
    print("Exception when calling RecordingsApi->get_recording_files: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

[**RecordingFilesGetResponse**](RecordingFilesGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of a recording&#39;s files |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recordings**
> RecordingsGetResponse get_recordings()

List all recordings

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")

try:
    # List all recordings
    data = api.get_recordings().result
    print(data)
except ApiException as e:
    print("Exception when calling RecordingsApi->get_recordings: %s\n" % e)


```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RecordingsGetResponse**](RecordingsGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of recordings |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_recording**
> RecordingPatchResponse patch_recording(recording_id, payload)

Update a recording

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
recording_id = 'recording_id_example' # str | 
payload = pupilcloud.RecordingPatchRequest() # RecordingPatchRequest | 

try:
    # Update a recording
    data = api.patch_recording(recording_id, payload).result
    print(data)
except ApiException as e:
    print("Exception when calling RecordingsApi->patch_recording: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 
 **payload** | [**RecordingPatchRequest**](RecordingPatchRequest.md)|  | 

### Return type

[**RecordingPatchResponse**](RecordingPatchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated recording |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**409** | Database conflict |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

