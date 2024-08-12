# pupilcloud.SurfacesApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_apriltag_detections**](SurfacesApi.md#get_apriltag_detections) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/apriltags | Get apritag data for surface enrichment
[**get_surface**](SurfacesApi.md#get_surface) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id} | Return surface definition
[**get_surface_corners**](SurfacesApi.md#get_surface_corners) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/surface_corners | get surface locations for surface enrichment
[**get_surface_detections_timeline**](SurfacesApi.md#get_surface_detections_timeline) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/recordings/{recording_id}/gaze_in_aoi_timeline | Recording surface detections
[**get_surface_gaze_on_aoi**](SurfacesApi.md#get_surface_gaze_on_aoi) | **GET** /workspaces/{workspace_id}/surfaces/{surface_id}/gaze_in_aoi | get gaze on aoi data for markerless enrichment
[**patch_rotate_surface_orientation**](SurfacesApi.md#patch_rotate_surface_orientation) | **PATCH** /workspaces/{workspace_id}/surfaces/{surface_id}/rotate | Change surface rotation
[**patch_surface**](SurfacesApi.md#patch_surface) | **PATCH** /workspaces/{workspace_id}/surfaces/{surface_id} | Update surface definition
[**post_distorted_surface_location**](SurfacesApi.md#post_distorted_surface_location) | **POST** /workspaces/{workspace_id}/surfaces/{surface_id}/set_distorted_location_using_recording | Set distorted surface corner locations
[**post_surface**](SurfacesApi.md#post_surface) | **POST** /workspaces/{workspace_id}/surfaces/ | Create a new surface definition


# **get_apriltag_detections**
> ApriltagDetectionsGetResponse get_apriltag_detections(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect)

Get apritag data for surface enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.apriltag_detections_get_response import ApriltagDetectionsGetResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | 
    end = 3.4 # float |  (optional)
    detect = 0 # int |  (optional) (default to 0)

    try:
        # Get apritag data for surface enrichment
        api_response = await api_instance.get_apriltag_detections(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect)
        print("The response of SurfacesApi->get_apriltag_detections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->get_apriltag_detections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **start** | **float**|  | 
 **end** | **float**|  | [optional] 
 **detect** | **int**|  | [optional] [default to 0]

### Return type

[**ApriltagDetectionsGetResponse**](ApriltagDetectionsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of apriltag detections |  -  |
**400** | Enrichment doesn&#39;t belong to surface id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Surface definition not found |  -  |
**405** | Project enrichment dosn&#39;t support surfaces |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface**
> SurfaceGetResponse get_surface(workspace_id, surface_id)

Return surface definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_get_response import SurfaceGetResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 

    try:
        # Return surface definition
        api_response = await api_instance.get_surface(workspace_id, surface_id)
        print("The response of SurfacesApi->get_surface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->get_surface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 

### Return type

[**SurfaceGetResponse**](SurfaceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Surface definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface_corners**
> SurfaceCornersGetResponse get_surface_corners(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect, distorted=distorted)

get surface locations for surface enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_corners_get_response import SurfaceCornersGetResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    start = 3.4 # float | 
    end = 3.4 # float |  (optional)
    detect = 0 # int |  (optional) (default to 0)
    distorted = False # bool |  (optional) (default to False)

    try:
        # get surface locations for surface enrichment
        api_response = await api_instance.get_surface_corners(workspace_id, surface_id, project_id, enrichment_id, recording_id, start, end=end, detect=detect, distorted=distorted)
        print("The response of SurfacesApi->get_surface_corners:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->get_surface_corners: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **start** | **float**|  | 
 **end** | **float**|  | [optional] 
 **detect** | **int**|  | [optional] [default to 0]
 **distorted** | **bool**|  | [optional] [default to False]

### Return type

[**SurfaceCornersGetResponse**](SurfaceCornersGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of surface locations |  -  |
**400** | Enrichment doesn&#39;t belong to surface id |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Surface definition not found |  -  |
**405** | Project enrichment dosn&#39;t support surfaces |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface_detections_timeline**
> SurfaceDetectionsTimelineGetResponse get_surface_detections_timeline(workspace_id, surface_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)

Recording surface detections

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_detections_timeline_get_response import SurfaceDetectionsTimelineGetResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    recording_id2 = 'recording_id_example' # str | recording id
    start = 3.4 # float | start time in seconds (optional)
    end = 3.4 # float | stop time in seconds (optional)
    intervalsize = 3.4 # float | size of interval buckets in seconds (optional)

    try:
        # Recording surface detections
        api_response = await api_instance.get_surface_detections_timeline(workspace_id, surface_id, recording_id, recording_id2, start=start, end=end, intervalsize=intervalsize)
        print("The response of SurfacesApi->get_surface_detections_timeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->get_surface_detections_timeline: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **recording_id2** | **str**| recording id | 
 **start** | **float**| start time in seconds | [optional] 
 **end** | **float**| stop time in seconds | [optional] 
 **intervalsize** | **float**| size of interval buckets in seconds | [optional] 

### Return type

[**SurfaceDetectionsTimelineGetResponse**](SurfaceDetectionsTimelineGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A timeline of surface detections |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_surface_gaze_on_aoi**
> SurfaceGazeOnAoiGetResponse get_surface_gaze_on_aoi(workspace_id, surface_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)

get gaze on aoi data for markerless enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_gaze_on_aoi_get_response import SurfaceGazeOnAoiGetResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    project_id = 'project_id_example' # str |  (optional)
    enrichment_id = 'enrichment_id_example' # str |  (optional)
    recording_id = 'recording_id_example' # str |  (optional)
    start = 3.4 # float |  (optional)
    end = 3.4 # float |  (optional)

    try:
        # get gaze on aoi data for markerless enrichment
        api_response = await api_instance.get_surface_gaze_on_aoi(workspace_id, surface_id, project_id=project_id, enrichment_id=enrichment_id, recording_id=recording_id, start=start, end=end)
        print("The response of SurfacesApi->get_surface_gaze_on_aoi:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->get_surface_gaze_on_aoi: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **project_id** | **str**|  | [optional] 
 **enrichment_id** | **str**|  | [optional] 
 **recording_id** | **str**|  | [optional] 
 **start** | **float**|  | [optional] 
 **end** | **float**|  | [optional] 

### Return type

[**SurfaceGazeOnAoiGetResponse**](SurfaceGazeOnAoiGetResponse.md)

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

# **patch_rotate_surface_orientation**
> patch_rotate_surface_orientation(workspace_id, surface_id, payload)

Change surface rotation

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.orientation_rotation import OrientationRotation
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    payload = pupilcloud.OrientationRotation() # OrientationRotation | 

    try:
        # Change surface rotation
        await api_instance.patch_rotate_surface_orientation(workspace_id, surface_id, payload)
    except Exception as e:
        print("Exception when calling SurfacesApi->patch_rotate_surface_orientation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **payload** | [**OrientationRotation**](OrientationRotation.md)|  | 

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
**200** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Surface definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_surface**
> SurfacePatchResponse patch_surface(workspace_id, surface_id, payload)

Update surface definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.patch_surface import PatchSurface
from pupilcloud.models.surface_patch_response import SurfacePatchResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    payload = pupilcloud.PatchSurface() # PatchSurface | 

    try:
        # Update surface definition
        api_response = await api_instance.patch_surface(workspace_id, surface_id, payload)
        print("The response of SurfacesApi->patch_surface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->patch_surface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **payload** | [**PatchSurface**](PatchSurface.md)|  | 

### Return type

[**SurfacePatchResponse**](SurfacePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Error updating surface |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Surface definition not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_distorted_surface_location**
> DistortedSurfaceLocationPostResponse post_distorted_surface_location(workspace_id, surface_id, payload)

Set distorted surface corner locations

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.distorted_surface_location_post_response import DistortedSurfaceLocationPostResponse
from pupilcloud.models.set_distorted_surface_request import SetDistortedSurfaceRequest
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    surface_id = 'surface_id_example' # str | 
    payload = pupilcloud.SetDistortedSurfaceRequest() # SetDistortedSurfaceRequest | 

    try:
        # Set distorted surface corner locations
        api_response = await api_instance.post_distorted_surface_location(workspace_id, surface_id, payload)
        print("The response of SurfacesApi->post_distorted_surface_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->post_distorted_surface_location: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **surface_id** | **str**|  | 
 **payload** | [**SetDistortedSurfaceRequest**](SetDistortedSurfaceRequest.md)|  | 

### Return type

[**DistortedSurfaceLocationPostResponse**](DistortedSurfaceLocationPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Surface corner coordinates |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Surface definition not found |  -  |
**501** | No markers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_surface**
> SurfacePostResponse post_surface(workspace_id, payload)

Create a new surface definition

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.surface_initialization import SurfaceInitialization
from pupilcloud.models.surface_post_response import SurfacePostResponse
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
    api_instance = pupilcloud.SurfacesApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.SurfaceInitialization() # SurfaceInitialization | 

    try:
        # Create a new surface definition
        api_response = await api_instance.post_surface(workspace_id, payload)
        print("The response of SurfacesApi->post_surface:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurfacesApi->post_surface: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**SurfaceInitialization**](SurfaceInitialization.md)|  | 

### Return type

[**SurfacePostResponse**](SurfacePostResponse.md)

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
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

