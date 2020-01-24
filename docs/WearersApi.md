# pupilcloud.WearersApi

All URIs are relative to *https://api.cloud.pupil-labs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_wearer**](WearersApi.md#delete_wearer) | **DELETE** /wearers/{wearer_id} | Delete a wearer
[**get_wearer**](WearersApi.md#get_wearer) | **GET** /wearers/{wearer_id} | Returns a wearer with {wearer_id}
[**get_wearers**](WearersApi.md#get_wearers) | **GET** /wearers/ | List all wearers
[**patch_wearer**](WearersApi.md#patch_wearer) | **PATCH** /wearers/{wearer_id} | Update a wearer
[**post_wearer**](WearersApi.md#post_wearer) | **POST** /wearers/ | Create a new wearer


# **delete_wearer**
> WearerDeleteResponse delete_wearer(wearer_id)

Delete a wearer

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
wearer_id = 'wearer_id_example' # str | 

try:
    # Delete a wearer
    data = api.delete_wearer(wearer_id).result
    print(data)
except ApiException as e:
    print("Exception when calling WearersApi->delete_wearer: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wearer_id** | **str**|  | 

### Return type

[**WearerDeleteResponse**](WearerDeleteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a single wearer |  -  |
**401** | Authentication is required |  -  |
**404** | Wearer doesn&#39;t exist |  -  |
**410** | Wearer was deleted |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wearer**
> WearerGetResponse get_wearer(wearer_id)

Returns a wearer with {wearer_id}

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
wearer_id = 'wearer_id_example' # str | 

try:
    # Returns a wearer with {wearer_id}
    data = api.get_wearer(wearer_id).result
    print(data)
except ApiException as e:
    print("Exception when calling WearersApi->get_wearer: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wearer_id** | **str**|  | 

### Return type

[**WearerGetResponse**](WearerGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single wearer |  -  |
**401** | Authentication is required |  -  |
**404** | Wearer doesn&#39;t exist |  -  |
**410** | Wearer was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wearers**
> WearersGetResponse get_wearers()

List all wearers

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")

try:
    # List all wearers
    data = api.get_wearers().result
    print(data)
except ApiException as e:
    print("Exception when calling WearersApi->get_wearers: %s\n" % e)


```


### Parameters
This endpoint does not need any parameter.

### Return type

[**WearersGetResponse**](WearersGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of wearers |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_wearer**
> WearerPatchResponse patch_wearer(wearer_id, payload)

Update a wearer

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
wearer_id = 'wearer_id_example' # str | 
payload = pupilcloud.WearerPatchRequest() # WearerPatchRequest | 

try:
    # Update a wearer
    data = api.patch_wearer(wearer_id, payload).result
    print(data)
except ApiException as e:
    print("Exception when calling WearersApi->patch_wearer: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wearer_id** | **str**|  | 
 **payload** | [**WearerPatchRequest**](WearerPatchRequest.md)|  | 

### Return type

[**WearerPatchResponse**](WearerPatchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated wearer |  -  |
**401** | Authentication is required |  -  |
**404** | Wearer doesn&#39;t exist |  -  |
**409** | Invalid input |  -  |
**410** | Wearer was deleted |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_wearer**
> WearerPostResponse post_wearer(payload)

Create a new wearer

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
payload = pupilcloud.WearerPostRequest() # WearerPostRequest | 

try:
    # Create a new wearer
    data = api.post_wearer(payload).result
    print(data)
except ApiException as e:
    print("Exception when calling WearersApi->post_wearer: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**WearerPostRequest**](WearerPostRequest.md)|  | 

### Return type

[**WearerPostResponse**](WearerPostResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created wearer |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

