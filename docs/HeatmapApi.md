# pupilcloud.HeatmapApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_download_heatmap**](HeatmapApi.md#get_download_heatmap) | **GET** /workspaces/{workspace_id}/heatmap/zip_download | download zip file with heatmaps
[**get_heatmap**](HeatmapApi.md#get_heatmap) | **GET** /workspaces/{workspace_id}/heatmap/ | get heatmap image or json data
[**get_heatmap_background**](HeatmapApi.md#get_heatmap_background) | **GET** /workspaces/{workspace_id}/heatmap/background | get heatmap background for overlay
[**post_download_heatmap**](HeatmapApi.md#post_download_heatmap) | **POST** /workspaces/{workspace_id}/heatmap/zip_download | download zip file with heatmaps
[**post_heatmap**](HeatmapApi.md#post_heatmap) | **POST** /workspaces/{workspace_id}/heatmap/ | get heatmap image or json data


# **get_download_heatmap**
> bytearray get_download_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)

download zip file with heatmaps

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
    api_instance = pupilcloud.HeatmapApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_ids = ['recording_ids_example'] # List[str] | Recordings UUIDs for which heatmap data is to be retrieved (optional)
    n_bins = 300 # int |  (optional) (default to 300)
    sigma = 0.05 # float |  (optional) (default to 0.05)
    height = 512 # int |  (optional) (default to 512)
    width = 512 # int |  (optional) (default to 512)
    max_size = 56 # int |  (optional)
    colormap = Turbo # str |  (optional) (default to Turbo)
    var_json = False # bool |  (optional) (default to False)

    try:
        # download zip file with heatmaps
        api_response = await api_instance.get_download_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)
        print("The response of HeatmapApi->get_download_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatmapApi->get_download_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_ids** | [**List[str]**](str.md)| Recordings UUIDs for which heatmap data is to be retrieved | [optional] 
 **n_bins** | **int**|  | [optional] [default to 300]
 **sigma** | **float**|  | [optional] [default to 0.05]
 **height** | **int**|  | [optional] [default to 512]
 **width** | **int**|  | [optional] [default to 512]
 **max_size** | **int**|  | [optional] 
 **colormap** | **str**|  | [optional] [default to Turbo]
 **var_json** | **bool**|  | [optional] [default to False]

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
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap**
> bytearray get_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)

get heatmap image or json data

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
    api_instance = pupilcloud.HeatmapApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    recording_ids = ['recording_ids_example'] # List[str] | Recordings UUIDs for which heatmap data is to be retrieved (optional)
    n_bins = 300 # int |  (optional) (default to 300)
    sigma = 0.05 # float |  (optional) (default to 0.05)
    height = 512 # int |  (optional) (default to 512)
    width = 512 # int |  (optional) (default to 512)
    max_size = 56 # int |  (optional)
    colormap = Turbo # str |  (optional) (default to Turbo)
    var_json = False # bool |  (optional) (default to False)

    try:
        # get heatmap image or json data
        api_response = await api_instance.get_heatmap(workspace_id, project_id, enrichment_id, recording_ids=recording_ids, n_bins=n_bins, sigma=sigma, height=height, width=width, max_size=max_size, colormap=colormap, var_json=var_json)
        print("The response of HeatmapApi->get_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatmapApi->get_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **recording_ids** | [**List[str]**](str.md)| Recordings UUIDs for which heatmap data is to be retrieved | [optional] 
 **n_bins** | **int**|  | [optional] [default to 300]
 **sigma** | **float**|  | [optional] [default to 0.05]
 **height** | **int**|  | [optional] [default to 512]
 **width** | **int**|  | [optional] [default to 512]
 **max_size** | **int**|  | [optional] 
 **colormap** | **str**|  | [optional] [default to Turbo]
 **var_json** | **bool**|  | [optional] [default to False]

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
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_heatmap_background**
> bytearray get_heatmap_background(workspace_id, project_id, enrichment_id, max_size=max_size)

get heatmap background for overlay

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
    api_instance = pupilcloud.HeatmapApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    project_id = 'project_id_example' # str | 
    enrichment_id = 'enrichment_id_example' # str | 
    max_size = 512 # int |  (optional) (default to 512)

    try:
        # get heatmap background for overlay
        api_response = await api_instance.get_heatmap_background(workspace_id, project_id, enrichment_id, max_size=max_size)
        print("The response of HeatmapApi->get_heatmap_background:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatmapApi->get_heatmap_background: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **project_id** | **str**|  | 
 **enrichment_id** | **str**|  | 
 **max_size** | **int**|  | [optional] [default to 512]

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
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_download_heatmap**
> bytearray post_download_heatmap(workspace_id, payload)

download zip file with heatmaps

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.generate_heatmap import GenerateHeatmap
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
    api_instance = pupilcloud.HeatmapApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.GenerateHeatmap() # GenerateHeatmap | 

    try:
        # download zip file with heatmaps
        api_response = await api_instance.post_download_heatmap(workspace_id, payload)
        print("The response of HeatmapApi->post_download_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatmapApi->post_download_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**GenerateHeatmap**](GenerateHeatmap.md)|  | 

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
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_heatmap**
> bytearray post_heatmap(workspace_id, payload)

get heatmap image or json data

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.generate_heatmap import GenerateHeatmap
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
    api_instance = pupilcloud.HeatmapApi(api_client)
    workspace_id = 'default' # str | Workspace UUID, can also use `default` for your personal workspace (default to 'default')
    payload = pupilcloud.GenerateHeatmap() # GenerateHeatmap | 

    try:
        # get heatmap image or json data
        api_response = await api_instance.post_heatmap(workspace_id, payload)
        print("The response of HeatmapApi->post_heatmap:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HeatmapApi->post_heatmap: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace UUID, can also use &#x60;default&#x60; for your personal workspace | [default to &#39;default&#39;]
 **payload** | [**GenerateHeatmap**](GenerateHeatmap.md)|  | 

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
**400** | Invalid value |  -  |
**401** | Authentication is required |  -  |
**403** | Permission denied. Allowed roles: {&#39;VIEWER&#39;, &#39;EDITOR&#39;, &#39;OWNER&#39;, &#39;DEMO&#39;, &#39;ADMIN&#39;} |  -  |
**404** | Enrichment doesn&#39;t exist |  -  |
**405** | Enrichment doesn&#39;t support heatmap |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

