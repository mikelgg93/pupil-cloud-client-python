# pupilcloud.MarkerlessApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_markerless**](MarkerlessApi.md#get_markerless) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id} | Get markerless definition
[**get_markerless_camera_poses**](MarkerlessApi.md#get_markerless_camera_poses) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/recordings/{recording_id}/camera_pose.{format} | get markerless camera poses
[**get_markerless_detections_timeline**](MarkerlessApi.md#get_markerless_detections_timeline) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/recordings/{recording_id}/gaze_in_aoi_timeline | Recording markerless detections
[**get_markerless_gaze_on_aoi**](MarkerlessApi.md#get_markerless_gaze_on_aoi) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/gaze_in_aoi | get gaze on aoi data for markerless enrichment
[**get_markerless_point_cloud**](MarkerlessApi.md#get_markerless_point_cloud) | **GET** /workspaces/{workspace_id}/markerless/{markerless_id}/point_cloud.{format} | 
[**initialize_markerless**](MarkerlessApi.md#initialize_markerless) | **POST** /workspaces/{workspace_id}/markerless/ | Create markerless definition
[**scan_markerless**](MarkerlessApi.md#scan_markerless) | **POST** /workspaces/{workspace_id}/markerless/{markerless_id}/scan | Scan markerless


# **get_markerless**
> MarkerlessGetResponse get_markerless(workspace_id, markerless_id)

Get markerless definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_get_response import MarkerlessGetResponse
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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 

    try:
        # Get markerless definition
        api_response = await api_instance.get_markerless(workspace_id, markerless_id)
        print("The response of MarkerlessApi->get_markerless:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerlessApi->get_markerless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 

### Return type

[**MarkerlessGetResponse**](MarkerlessGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Markerless scanning definition |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Markerless definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_camera_poses**
> MarkerlessCameraPosesGetResponse get_markerless_camera_poses(workspace_id, markerless_id, recording_id, format, start=start, end=end, limit=limit)

get markerless camera poses

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_camera_poses_get_response import MarkerlessCameraPosesGetResponse
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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    format = 'format_example' # str | 
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)
    limit = 56 # int |  (optional)

    try:
        # get markerless camera poses
        api_response = await api_instance.get_markerless_camera_poses(workspace_id, markerless_id, recording_id, format, start=start, end=end, limit=limit)
        print("The response of MarkerlessApi->get_markerless_camera_poses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerlessApi->get_markerless_camera_poses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **format** | **str**|  | 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**MarkerlessCameraPosesGetResponse**](MarkerlessCameraPosesGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of markerless camera pose |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_detections_timeline**
> MarkerlessDetectionsTimelineGetResponse get_markerless_detections_timeline(workspace_id, markerless_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)

Recording markerless detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_detections_timeline_get_response import MarkerlessDetectionsTimelineGetResponse
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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    recording_id2 = 'recording_id_example' # str | recording id
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording markerless detections
        api_response = await api_instance.get_markerless_detections_timeline(workspace_id, markerless_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)
        print("The response of MarkerlessApi->get_markerless_detections_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerlessApi->get_markerless_detections_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **recording_id2** | **str**| recording id | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**MarkerlessDetectionsTimelineGetResponse**](MarkerlessDetectionsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of markerless detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_gaze_on_aoi**
> MarkerlessGazeOnAoiGetResponse get_markerless_gaze_on_aoi(workspace_id, markerless_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)

get gaze on aoi data for markerless enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_gaze_on_aoi_get_response import MarkerlessGazeOnAoiGetResponse
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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    project_id = 'project_id_example' # str |  (optional)
    enrichment_id = 'enrichment_id_example' # str |  (optional)
    recording_id = 'recording_id_example' # str |  (optional)
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)

    try:
        # get gaze on aoi data for markerless enrichment
        api_response = await api_instance.get_markerless_gaze_on_aoi(workspace_id, markerless_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)
        print("The response of MarkerlessApi->get_markerless_gaze_on_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerlessApi->get_markerless_gaze_on_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **project_id** | **str**|  | [optional] 
 **enrichment_id** | **str**|  | [optional] 
 **recording_id** | **str**|  | [optional] 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 

### Return type

[**MarkerlessGazeOnAoiGetResponse**](MarkerlessGazeOnAoiGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of gaze in aoi coordinates with time ranges |  -  |
**400** | Enrichment doesn&#39;t belong to markerless id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Markerless definition not found |  -  |
**405** | Enrichment does not support markerless |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_markerless_point_cloud**
> MarkerlessPointCloudGetResponse get_markerless_point_cloud(workspace_id, markerless_id, format, limit=limit)



### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.markerless_point_cloud_get_response import MarkerlessPointCloudGetResponse
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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 
    format = 'format_example' # str | 
    limit = 56 # int |  (optional)

    try:
        api_response = await api_instance.get_markerless_point_cloud(workspace_id, markerless_id, format, limit=limit)
        print("The response of MarkerlessApi->get_markerless_point_cloud:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerlessApi->get_markerless_point_cloud: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 
 **format** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**MarkerlessPointCloudGetResponse**](MarkerlessPointCloudGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of markerless point cloud |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_markerless**
> InitializeMarkerlessResponse initialize_markerless(workspace_id, payload)

Create markerless definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.initialize_markerless_response import InitializeMarkerlessResponse
from pupilcloud.models.markerless_initialization import MarkerlessInitialization
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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.MarkerlessInitialization() # MarkerlessInitialization | 

    try:
        # Create markerless definition
        api_response = await api_instance.initialize_markerless(workspace_id, payload)
        print("The response of MarkerlessApi->initialize_markerless:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkerlessApi->initialize_markerless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**MarkerlessInitialization**](MarkerlessInitialization.md)|  | 

### Return type

[**InitializeMarkerlessResponse**](InitializeMarkerlessResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_markerless**
> scan_markerless(workspace_id, markerless_id)

Scan markerless

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
    api_instance = pupilcloud.MarkerlessApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    markerless_id = 'markerless_id_example' # str | 

    try:
        # Scan markerless
        await api_instance.scan_markerless(workspace_id, markerless_id)
    except Exception as e:
        print("Exception when calling MarkerlessApi->scan_markerless: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **markerless_id** | **str**|  | 

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
**200** | Successful operation |  -  |
**400** | Markerless definition not found |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

