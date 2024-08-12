# pupilcloud.ProjectsApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_static_image_mapper_enrichments_recording_fixation**](ProjectsApi.md#clear_static_image_mapper_enrichments_recording_fixation) | **POST** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations:clear | Clear or resets all the mapped fixation of recording&#39;s
[**delete_project_enrichment_resource**](ProjectsApi.md#delete_project_enrichment_resource) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id} | Delete a project enrichment
[**delete_project_recording_event_resource**](ProjectsApi.md#delete_project_recording_event_resource) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events/{event_id} | Delete a project recording event
[**delete_project_resource**](ProjectsApi.md#delete_project_resource) | **DELETE** /workspaces/{workspace_id}/projects/{project_id} | Delete a project
[**delete_projects_resource**](ProjectsApi.md#delete_projects_resource) | **DELETE** /workspaces/{workspace_id}/projects/ | Delete multiple projects
[**delete_static_image_mapper_enrichments_recording_fixation**](ProjectsApi.md#delete_static_image_mapper_enrichments_recording_fixation) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations/{fixation_id} | Deletes coordinates of a particular fixation of recording&#39;s
[**delete_visualization_config**](ProjectsApi.md#delete_visualization_config) | **DELETE** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs/{visualization_config_id} | Delete a visualization config
[**export_static_image_mapper_enrichment**](ProjectsApi.md#export_static_image_mapper_enrichment) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{static_enrichment_id}/export | Export static image mapper enrichment
[**get_project_enrichment**](ProjectsApi.md#get_project_enrichment) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id} | Get a project enrichment
[**get_project_enrichment_compute_resource**](ProjectsApi.md#get_project_enrichment_compute_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/compute | 
[**get_project_enrichments**](ProjectsApi.md#get_project_enrichments) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments | List all project enrichments
[**get_project_events_resource**](ProjectsApi.md#get_project_events_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/events/ | Returns a project&#39;s events with {project_id}
[**get_project_recording_events_resource**](ProjectsApi.md#get_project_recording_events_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events | Returns a project&#39;s recording event with {project_id} and {recording_id}
[**get_project_recordings_resource**](ProjectsApi.md#get_project_recordings_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id}/recordings/ | Returns a project&#39;s recordings with {project_id}
[**get_project_resource**](ProjectsApi.md#get_project_resource) | **GET** /workspaces/{workspace_id}/projects/{project_id} | Returns a project with {project_id}
[**get_project_unique_events**](ProjectsApi.md#get_project_unique_events) | **GET** /workspaces/{workspace_id}/projects/{project_id}/unique-events/ | Returns all unique events in a project
[**get_projects_resource**](ProjectsApi.md#get_projects_resource) | **GET** /workspaces/{workspace_id}/projects/ | List all projects
[**get_static_image_mapper_enrichment**](ProjectsApi.md#get_static_image_mapper_enrichment) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{static_enrichment_id} | Get a static image mapper enrichment
[**get_static_image_mapper_enrichments**](ProjectsApi.md#get_static_image_mapper_enrichments) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/ | List all static image mapper enrichments of a project
[**get_static_image_mapper_enrichments_recording_fixations**](ProjectsApi.md#get_static_image_mapper_enrichments_recording_fixations) | **GET** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations | List all the fixations of a recording&#39;s static image mapper enrichments
[**get_visualization_config**](ProjectsApi.md#get_visualization_config) | **GET** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs/{visualization_config_id} | Get a visualization config
[**get_visualization_configs**](ProjectsApi.md#get_visualization_configs) | **GET** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs | List project&#39;s visualization configs
[**patch_project_enrichment_resource**](ProjectsApi.md#patch_project_enrichment_resource) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id} | Update a project enrichment
[**patch_project_recording_event_resource**](ProjectsApi.md#patch_project_recording_event_resource) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events/{event_id} | Update a project recording event
[**patch_project_resource**](ProjectsApi.md#patch_project_resource) | **PATCH** /workspaces/{workspace_id}/projects/{project_id} | Update a project
[**patch_static_image_mapper_enrichment**](ProjectsApi.md#patch_static_image_mapper_enrichment) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{static_enrichment_id} | Update a static image mapper enrichment
[**patch_visualization_config**](ProjectsApi.md#patch_visualization_config) | **PATCH** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs/{visualization_config_id} | Update a visualization config
[**post_project_download_resource**](ProjectsApi.md#post_project_download_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/download | Download project data
[**post_project_enrichment**](ProjectsApi.md#post_project_enrichment) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments | Create a new project enrichment
[**post_project_enrichment_cancel_resource**](ProjectsApi.md#post_project_enrichment_cancel_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/cancel | 
[**post_project_enrichment_compute_resource**](ProjectsApi.md#post_project_enrichment_compute_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/compute | 
[**post_project_enrichment_export_resource**](ProjectsApi.md#post_project_enrichment_export_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/export | Export an enrichment data
[**post_project_recording_events_resource**](ProjectsApi.md#post_project_recording_events_resource) | **POST** /workspaces/{workspace_id}/projects/{project_id}/recordings/{recording_id}/events | Create a new project recording event
[**post_projects_resource**](ProjectsApi.md#post_projects_resource) | **POST** /workspaces/{workspace_id}/projects/ | Create a new project
[**post_static_image_mapper_enrichment**](ProjectsApi.md#post_static_image_mapper_enrichment) | **POST** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/ | Create a new static image mapper enrichment
[**post_visualization_config**](ProjectsApi.md#post_visualization_config) | **POST** /workspaces/{workspace_id}/projects/{project_id}/visualization_configs | Create a new visualization config
[**project_enrichments_export**](ProjectsApi.md#project_enrichments_export) | **GET** /workspaces/{workspace_id}/projects/{project_id}/enrichments/{enrichment_id}/export | Export an enrichment data
[**put_static_image_mapper_enrichments_recording_fixation**](ProjectsApi.md#put_static_image_mapper_enrichments_recording_fixation) | **PUT** /workspaces/{workspace_id}/projects/{project_id}/mappers/static/{enrichment_id}/recordings/{recording_id}/fixations/{fixation_id} | Insert or update coordinates of a particular fixation of recording&#39;s


# **clear_static_image_mapper_enrichments_recording_fixation**
> clear_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id)

Clear or resets all the mapped fixation of recording's

static image mapper enrichments

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 

    try:
        # Clear or resets all the mapped fixation of recording's
        await api_instance.clear_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->clear_static_image_mapper_enrichments_recording_fixation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
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
**200** | Cleared manually mapped fixation data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Enrichment or Recording is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_enrichment_resource**
> delete_project_enrichment_resource(workspace_id, project_id, enrichment_id)

Delete a project enrichment

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        # Delete a project enrichment
        await api_instance.delete_project_enrichment_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_enrichment_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

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
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_recording_event_resource**
> delete_project_recording_event_resource(workspace_id, project_id, recording_id, event_id)

Delete a project recording event

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 

    try:
        # Delete a project recording event
        await api_instance.delete_project_recording_event_resource(workspace_id, project_id, recording_id, event_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 

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

# **delete_project_resource**
> delete_project_resource(workspace_id, project_id)

Delete a project

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Delete a project
        await api_instance.delete_project_resource(workspace_id, project_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

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
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_projects_resource**
> delete_projects_resource(workspace_id, payload)

Delete multiple projects

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.projects_delete_request import ProjectsDeleteRequest
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.ProjectsDeleteRequest() # ProjectsDeleteRequest | 

    try:
        # Delete multiple projects
        await api_instance.delete_projects_resource(workspace_id, payload)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_projects_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**ProjectsDeleteRequest**](ProjectsDeleteRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_image_mapper_enrichments_recording_fixation**
> delete_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id)

Deletes coordinates of a particular fixation of recording's

static image mapper enrichments

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    fixation_id = 56 # int | 

    try:
        # Deletes coordinates of a particular fixation of recording's
        await api_instance.delete_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_static_image_mapper_enrichments_recording_fixation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **fixation_id** | **int**|  | 

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
**200** | Resource deleted |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Enrichment or Recording or fixations.json or event section or fixation coordinates are not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_visualization_config**
> VisualizationConfigDeleteResponse delete_visualization_config(workspace_id, project_id, visualization_config_id)

Delete a visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_delete_response import VisualizationConfigDeleteResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    visualization_config_id = 'visualization_config_id_example' # str | 

    try:
        # Delete a visualization config
        api_response = await api_instance.delete_visualization_config(workspace_id, project_id, visualization_config_id)
        print("The response of ProjectsApi->delete_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **visualization_config_id** | **str**|  | 

### Return type

[**VisualizationConfigDeleteResponse**](VisualizationConfigDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a visualization config |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Visualization config not found |  -  |
**410** | Visualization config deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_static_image_mapper_enrichment**
> export_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)

Export static image mapper enrichment

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    static_enrichment_id = 'static_enrichment_id_example' # str | 

    try:
        # Export static image mapper enrichment
        await api_instance.export_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->export_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **static_enrichment_id** | **str**|  | 

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
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Static image mapper enrichment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_enrichment**
> ProjectEnrichmentGetResponse get_project_enrichment(workspace_id, project_id, enrichment_id)

Get a project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_get_response import ProjectEnrichmentGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        # Get a project enrichment
        api_response = await api_instance.get_project_enrichment(workspace_id, project_id, enrichment_id)
        print("The response of ProjectsApi->get_project_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

### Return type

[**ProjectEnrichmentGetResponse**](ProjectEnrichmentGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project enrichment |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_enrichment_compute_resource**
> get_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)



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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        await api_instance.get_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_enrichment_compute_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

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
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_enrichments**
> ProjectEnrichmentsGetResponse get_project_enrichments(workspace_id, project_id)

List all project enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichments_get_response import ProjectEnrichmentsGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # List all project enrichments
        api_response = await api_instance.get_project_enrichments(workspace_id, project_id)
        print("The response of ProjectsApi->get_project_enrichments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_enrichments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectEnrichmentsGetResponse**](ProjectEnrichmentsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of project enrichments |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_events_resource**
> ProjectEventsResourceGetResponse get_project_events_resource(workspace_id, project_id)

Returns a project's events with {project_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_events_resource_get_response import ProjectEventsResourceGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns a project's events with {project_id}
        api_response = await api_instance.get_project_events_resource(workspace_id, project_id)
        print("The response of ProjectsApi->get_project_events_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectEventsResourceGetResponse**](ProjectEventsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project recording events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_recording_events_resource**
> ProjectRecordingEventsResourceGetResponse get_project_recording_events_resource(workspace_id, project_id, recording_id)

Returns a project's recording event with {project_id} and {recording_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recording_events_resource_get_response import ProjectRecordingEventsResourceGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 

    try:
        # Returns a project's recording event with {project_id} and {recording_id}
        api_response = await api_instance.get_project_recording_events_resource(workspace_id, project_id, recording_id)
        print("The response of ProjectsApi->get_project_recording_events_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_recording_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 

### Return type

[**ProjectRecordingEventsResourceGetResponse**](ProjectRecordingEventsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project&#39;s recording events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_recordings_resource**
> ProjectRecordingsResourceGetResponse get_project_recordings_resource(workspace_id, project_id)

Returns a project's recordings with {project_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recordings_resource_get_response import ProjectRecordingsResourceGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns a project's recordings with {project_id}
        api_response = await api_instance.get_project_recordings_resource(workspace_id, project_id)
        print("The response of ProjectsApi->get_project_recordings_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_recordings_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectRecordingsResourceGetResponse**](ProjectRecordingsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project&#39;s recordings |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_resource**
> ProjectResourceGetResponse get_project_resource(workspace_id, project_id)

Returns a project with {project_id}

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_resource_get_response import ProjectResourceGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns a project with {project_id}
        api_response = await api_instance.get_project_resource(workspace_id, project_id)
        print("The response of ProjectsApi->get_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectResourceGetResponse**](ProjectResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single project |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_unique_events**
> ProjectUniqueEventsGetResponse get_project_unique_events(workspace_id, project_id)

Returns all unique events in a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_unique_events_get_response import ProjectUniqueEventsGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # Returns all unique events in a project
        api_response = await api_instance.get_project_unique_events(workspace_id, project_id)
        print("The response of ProjectsApi->get_project_unique_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_unique_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**ProjectUniqueEventsGetResponse**](ProjectUniqueEventsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A project&#39;s unique events |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_resource**
> ProjectsResourceGetResponse get_projects_resource(workspace_id)

List all projects

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.projects_resource_get_response import ProjectsResourceGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')

    try:
        # List all projects
        api_response = await api_instance.get_projects_resource(workspace_id)
        print("The response of ProjectsApi->get_projects_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]

### Return type

[**ProjectsResourceGetResponse**](ProjectsResourceGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of projects |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_image_mapper_enrichment**
> StaticImageMapperEnrichmentGetResponse get_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)

Get a static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichment_get_response import StaticImageMapperEnrichmentGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    static_enrichment_id = 'static_enrichment_id_example' # str | 

    try:
        # Get a static image mapper enrichment
        api_response = await api_instance.get_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id)
        print("The response of ProjectsApi->get_static_image_mapper_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **static_enrichment_id** | **str**|  | 

### Return type

[**StaticImageMapperEnrichmentGetResponse**](StaticImageMapperEnrichmentGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A static image mapper enrichment |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Static image mapper enrichment not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_image_mapper_enrichments**
> StaticImageMapperEnrichmentsGetResponse get_static_image_mapper_enrichments(workspace_id, project_id)

List all static image mapper enrichments of a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichments_get_response import StaticImageMapperEnrichmentsGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # List all static image mapper enrichments of a project
        api_response = await api_instance.get_static_image_mapper_enrichments(workspace_id, project_id)
        print("The response of ProjectsApi->get_static_image_mapper_enrichments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_static_image_mapper_enrichments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**StaticImageMapperEnrichmentsGetResponse**](StaticImageMapperEnrichmentsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of static image mapper enrichments of a project |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_image_mapper_enrichments_recording_fixations**
> StaticImageMapperEnrichmentsRecordingFixationsGetResponse get_static_image_mapper_enrichments_recording_fixations(workspace_id, project_id, enrichment_id, recording_id)

List all the fixations of a recording's static image mapper enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichments_recording_fixations_get_response import StaticImageMapperEnrichmentsRecordingFixationsGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 

    try:
        # List all the fixations of a recording's static image mapper enrichments
        api_response = await api_instance.get_static_image_mapper_enrichments_recording_fixations(workspace_id, project_id, enrichment_id, recording_id)
        print("The response of ProjectsApi->get_static_image_mapper_enrichments_recording_fixations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_static_image_mapper_enrichments_recording_fixations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 

### Return type

[**StaticImageMapperEnrichmentsRecordingFixationsGetResponse**](StaticImageMapperEnrichmentsRecordingFixationsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fixations details along with total and mapped fixations count |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment or Recording or fixations.json or event section is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visualization_config**
> VisualizationConfigGetResponse get_visualization_config(workspace_id, project_id, visualization_config_id)

Get a visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_get_response import VisualizationConfigGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    visualization_config_id = 'visualization_config_id_example' # str | 

    try:
        # Get a visualization config
        api_response = await api_instance.get_visualization_config(workspace_id, project_id, visualization_config_id)
        print("The response of ProjectsApi->get_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **visualization_config_id** | **str**|  | 

### Return type

[**VisualizationConfigGetResponse**](VisualizationConfigGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A visualization config |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Visualization config not found |  -  |
**410** | Visualization config deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visualization_configs**
> VisualizationConfigsGetResponse get_visualization_configs(workspace_id, project_id)

List project's visualization configs

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_configs_get_response import VisualizationConfigsGetResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 

    try:
        # List project's visualization configs
        api_response = await api_instance.get_visualization_configs(workspace_id, project_id)
        print("The response of ProjectsApi->get_visualization_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_visualization_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 

### Return type

[**VisualizationConfigsGetResponse**](VisualizationConfigsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of project&#39;s visualization configs |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_enrichment_resource**
> ProjectEnrichmentResourcePatchResponse patch_project_enrichment_resource(workspace_id, project_id, enrichment_id, payload)

Update a project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_patch_request import ProjectEnrichmentPatchRequest
from pupilcloud.models.project_enrichment_resource_patch_response import ProjectEnrichmentResourcePatchResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.ProjectEnrichmentPatchRequest() # ProjectEnrichmentPatchRequest | 

    try:
        # Update a project enrichment
        api_response = await api_instance.patch_project_enrichment_resource(workspace_id, project_id, enrichment_id, payload)
        print("The response of ProjectsApi->patch_project_enrichment_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_project_enrichment_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**ProjectEnrichmentPatchRequest**](ProjectEnrichmentPatchRequest.md)|  | 

### Return type

[**ProjectEnrichmentResourcePatchResponse**](ProjectEnrichmentResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated project enrichment |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project_recording_event_resource**
> ProjectRecordingEventResourcePatchResponse patch_project_recording_event_resource(workspace_id, project_id, recording_id, event_id, payload)

Update a project recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recording_event_patch_request import ProjectRecordingEventPatchRequest
from pupilcloud.models.project_recording_event_resource_patch_response import ProjectRecordingEventResourcePatchResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    event_id = 'event_id_example' # str | 
    payload = pupilcloud.ProjectRecordingEventPatchRequest() # ProjectRecordingEventPatchRequest | 

    try:
        # Update a project recording event
        api_response = await api_instance.patch_project_recording_event_resource(workspace_id, project_id, recording_id, event_id, payload)
        print("The response of ProjectsApi->patch_project_recording_event_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_project_recording_event_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **event_id** | **str**|  | 
 **payload** | [**ProjectRecordingEventPatchRequest**](ProjectRecordingEventPatchRequest.md)|  | 

### Return type

[**ProjectRecordingEventResourcePatchResponse**](ProjectRecordingEventResourcePatchResponse.md)

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

# **patch_project_resource**
> ProjectResourcePatchResponse patch_project_resource(workspace_id, project_id, payload)

Update a project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_patch_request import ProjectPatchRequest
from pupilcloud.models.project_resource_patch_response import ProjectResourcePatchResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.ProjectPatchRequest() # ProjectPatchRequest | 

    try:
        # Update a project
        api_response = await api_instance.patch_project_resource(workspace_id, project_id, payload)
        print("The response of ProjectsApi->patch_project_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_project_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**ProjectPatchRequest**](ProjectPatchRequest.md)|  | 

### Return type

[**ProjectResourcePatchResponse**](ProjectResourcePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated project |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Database conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_static_image_mapper_enrichment**
> StaticImageMapperEnrichmentPatchResponse patch_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id, payload)

Update a static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichment_patch_response import StaticImageMapperEnrichmentPatchResponse
from pupilcloud.models.static_image_mapper_patch_request import StaticImageMapperPatchRequest
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    static_enrichment_id = 'static_enrichment_id_example' # str | 
    payload = pupilcloud.StaticImageMapperPatchRequest() # StaticImageMapperPatchRequest | 

    try:
        # Update a static image mapper enrichment
        api_response = await api_instance.patch_static_image_mapper_enrichment(workspace_id, project_id, static_enrichment_id, payload)
        print("The response of ProjectsApi->patch_static_image_mapper_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **static_enrichment_id** | **str**|  | 
 **payload** | [**StaticImageMapperPatchRequest**](StaticImageMapperPatchRequest.md)|  | 

### Return type

[**StaticImageMapperEnrichmentPatchResponse**](StaticImageMapperEnrichmentPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated static image mapper enrichment |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**404** | Static image mapper enrichment not found |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_visualization_config**
> VisualizationConfigPatchResponse patch_visualization_config(workspace_id, project_id, visualization_config_id, payload)

Update a visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_patch_request import VisualizationConfigPatchRequest
from pupilcloud.models.visualization_config_patch_response import VisualizationConfigPatchResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    visualization_config_id = 'visualization_config_id_example' # str | 
    payload = pupilcloud.VisualizationConfigPatchRequest() # VisualizationConfigPatchRequest | 

    try:
        # Update a visualization config
        api_response = await api_instance.patch_visualization_config(workspace_id, project_id, visualization_config_id, payload)
        print("The response of ProjectsApi->patch_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **visualization_config_id** | **str**|  | 
 **payload** | [**VisualizationConfigPatchRequest**](VisualizationConfigPatchRequest.md)|  | 

### Return type

[**VisualizationConfigPatchResponse**](VisualizationConfigPatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated visualization config |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Visualization config not found |  -  |
**410** | Visualization config deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_download_resource**
> post_project_download_resource(workspace_id, project_id, payload)

Download project data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_download_request import ProjectDownloadRequest
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.ProjectDownloadRequest() # ProjectDownloadRequest | 

    try:
        # Download project data
        await api_instance.post_project_download_resource(workspace_id, project_id, payload)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_download_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**ProjectDownloadRequest**](ProjectDownloadRequest.md)|  | 

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
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment**
> ProjectEnrichmentPostResponse post_project_enrichment(workspace_id, project_id, payload)

Create a new project enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_post_request import ProjectEnrichmentPostRequest
from pupilcloud.models.project_enrichment_post_response import ProjectEnrichmentPostResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.ProjectEnrichmentPostRequest() # ProjectEnrichmentPostRequest | 

    try:
        # Create a new project enrichment
        api_response = await api_instance.post_project_enrichment(workspace_id, project_id, payload)
        print("The response of ProjectsApi->post_project_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**ProjectEnrichmentPostRequest**](ProjectEnrichmentPostRequest.md)|  | 

### Return type

[**ProjectEnrichmentPostResponse**](ProjectEnrichmentPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created project enrichment |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment_cancel_resource**
> post_project_enrichment_cancel_resource(workspace_id, project_id, enrichment_id)



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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        await api_instance.post_project_enrichment_cancel_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_enrichment_cancel_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

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
**403** | Permission denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment_compute_resource**
> post_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)



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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 

    try:
        await api_instance.post_project_enrichment_compute_resource(workspace_id, project_id, enrichment_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_enrichment_compute_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 

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
**403** | Permission denied |  -  |
**405** | Enrichment not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_enrichment_export_resource**
> bytearray post_project_enrichment_export_resource(workspace_id, project_id, enrichment_id, payload)

Export an enrichment data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_enrichment_export import ProjectEnrichmentExport
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    payload = pupilcloud.ProjectEnrichmentExport() # ProjectEnrichmentExport | 

    try:
        # Export an enrichment data
        api_response = await api_instance.post_project_enrichment_export_resource(workspace_id, project_id, enrichment_id, payload)
        print("The response of ProjectsApi->post_project_enrichment_export_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_enrichment_export_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **payload** | [**ProjectEnrichmentExport**](ProjectEnrichmentExport.md)|  | 

### Return type

**bytearray**

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Binary file data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | ProjectEnrichment doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_project_recording_events_resource**
> ProjectRecordingEventsResourcePostResponse post_project_recording_events_resource(workspace_id, project_id, recording_id, payload)

Create a new project recording event

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_recording_event_post_request import ProjectRecordingEventPostRequest
from pupilcloud.models.project_recording_events_resource_post_response import ProjectRecordingEventsResourcePostResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    payload = pupilcloud.ProjectRecordingEventPostRequest() # ProjectRecordingEventPostRequest | 

    try:
        # Create a new project recording event
        api_response = await api_instance.post_project_recording_events_resource(workspace_id, project_id, recording_id, payload)
        print("The response of ProjectsApi->post_project_recording_events_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_recording_events_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **payload** | [**ProjectRecordingEventPostRequest**](ProjectRecordingEventPostRequest.md)|  | 

### Return type

[**ProjectRecordingEventsResourcePostResponse**](ProjectRecordingEventsResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created project recording event |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_projects_resource**
> ProjectsResourcePostResponse post_projects_resource(workspace_id, payload)

Create a new project

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.project_post_request import ProjectPostRequest
from pupilcloud.models.projects_resource_post_response import ProjectsResourcePostResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.ProjectPostRequest() # ProjectPostRequest | 

    try:
        # Create a new project
        api_response = await api_instance.post_projects_resource(workspace_id, payload)
        print("The response of ProjectsApi->post_projects_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_projects_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**ProjectPostRequest**](ProjectPostRequest.md)|  | 

### Return type

[**ProjectsResourcePostResponse**](ProjectsResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created project |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_static_image_mapper_enrichment**
> StaticImageMapperEnrichmentPostResponse post_static_image_mapper_enrichment(workspace_id, project_id, payload)

Create a new static image mapper enrichment

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichment_post_response import StaticImageMapperEnrichmentPostResponse
from pupilcloud.models.static_image_mapper_post_request import StaticImageMapperPostRequest
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.StaticImageMapperPostRequest() # StaticImageMapperPostRequest | 

    try:
        # Create a new static image mapper enrichment
        api_response = await api_instance.post_static_image_mapper_enrichment(workspace_id, project_id, payload)
        print("The response of ProjectsApi->post_static_image_mapper_enrichment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_static_image_mapper_enrichment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**StaticImageMapperPostRequest**](StaticImageMapperPostRequest.md)|  | 

### Return type

[**StaticImageMapperEnrichmentPostResponse**](StaticImageMapperEnrichmentPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created static image mapper enrichment |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_visualization_config**
> VisualizationConfigPostResponse post_visualization_config(workspace_id, project_id, payload)

Create a new visualization config

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.visualization_config_post_request import VisualizationConfigPostRequest
from pupilcloud.models.visualization_config_post_response import VisualizationConfigPostResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    payload = pupilcloud.VisualizationConfigPostRequest() # VisualizationConfigPostRequest | 

    try:
        # Create a new visualization config
        api_response = await api_instance.post_visualization_config(workspace_id, project_id, payload)
        print("The response of ProjectsApi->post_visualization_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_visualization_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **payload** | [**VisualizationConfigPostRequest**](VisualizationConfigPostRequest.md)|  | 

### Return type

[**VisualizationConfigPostResponse**](VisualizationConfigPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created visualization config |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **project_enrichments_export**
> bytearray project_enrichments_export(workspace_id, project_id, enrichment_id, recording_ids=recording_ids)

Export an enrichment data

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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_ids = ['recording_ids_example'] # List[str] | Recordings UUIDs for which data is to be exported (optional)

    try:
        # Export an enrichment data
        api_response = await api_instance.project_enrichments_export(workspace_id, project_id, enrichment_id, recording_ids=recording_ids)
        print("The response of ProjectsApi->project_enrichments_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->project_enrichments_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_ids** | [**List[str]**](str.md)| Recordings UUIDs for which data is to be exported | [optional] 

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
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | ProjectEnrichment doesn&#39;t exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_static_image_mapper_enrichments_recording_fixation**
> StaticImageMapperEnrichmentsRecordingFixationPutResponse put_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id, payload)

Insert or update coordinates of a particular fixation of recording's

static image mapper enrichments

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.static_image_mapper_enrichments_recording_fixation_put_response import StaticImageMapperEnrichmentsRecordingFixationPutResponse
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
    api_instance = pupilcloud.ProjectsApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_id = 'recording_id_example' # str | 
    fixation_id = 56 # int | 
    payload = None # object | 

    try:
        # Insert or update coordinates of a particular fixation of recording's
        api_response = await api_instance.put_static_image_mapper_enrichments_recording_fixation(workspace_id, project_id, enrichment_id, recording_id, fixation_id, payload)
        print("The response of ProjectsApi->put_static_image_mapper_enrichments_recording_fixation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->put_static_image_mapper_enrichments_recording_fixation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_id** | **str**|  | 
 **fixation_id** | **int**|  | 
 **payload** | **object**|  | 

### Return type

[**StaticImageMapperEnrichmentsRecordingFixationPutResponse**](StaticImageMapperEnrichmentsRecordingFixationPutResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Particular fixation data of that recording |  -  |
**201** | Updated fixation data |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;OWNER&#39;, &#39;ADMIN&#39;, &#39;DEMO&#39;, &#39;EDITOR&#39;} |  -  |
**404** | Enrichment or Recording or fixations.json or event section is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

