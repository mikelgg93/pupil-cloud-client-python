# pupilcloud.LabelsApi

All URIs are relative to *https://api.cloud.pupil-labs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_label**](LabelsApi.md#delete_label) | **DELETE** /labels/{label_id} | Delete a label
[**get_label**](LabelsApi.md#get_label) | **GET** /labels/{label_id} | Returns a label with {label_id}
[**get_labels**](LabelsApi.md#get_labels) | **GET** /labels/ | List all labels
[**patch_label**](LabelsApi.md#patch_label) | **PATCH** /labels/{label_id} | Update a label
[**post_label**](LabelsApi.md#post_label) | **POST** /labels/ | Create a new label


# **delete_label**
> delete_label(label_id)

Delete a label

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
label_id = 'label_id_example' # str | 

try:
    # Delete a label
    api.delete_label(label_id)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_label: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**|  | 

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

# **get_label**
> LabelGetResponse get_label(label_id)

Returns a label with {label_id}

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
label_id = 'label_id_example' # str | 

try:
    # Returns a label with {label_id}
    data = api.get_label(label_id).result
    print(data)
except ApiException as e:
    print("Exception when calling LabelsApi->get_label: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**|  | 

### Return type

[**LabelGetResponse**](LabelGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single label |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_labels**
> LabelsGetResponse get_labels()

List all labels

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")

try:
    # List all labels
    data = api.get_labels().result
    print(data)
except ApiException as e:
    print("Exception when calling LabelsApi->get_labels: %s\n" % e)


```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LabelsGetResponse**](LabelsGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of labels |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_label**
> LabelPatchResponse patch_label(label_id, payload)

Update a label

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
label_id = 'label_id_example' # str | 
payload = pupilcloud.LabelPatchRequest() # LabelPatchRequest | 

try:
    # Update a label
    data = api.patch_label(label_id, payload).result
    print(data)
except ApiException as e:
    print("Exception when calling LabelsApi->patch_label: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **label_id** | **str**|  | 
 **payload** | [**LabelPatchRequest**](LabelPatchRequest.md)|  | 

### Return type

[**LabelPatchResponse**](LabelPatchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated label |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**409** | Database conflict |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_label**
> LabelPostResponse post_label(payload)

Create a new label

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
payload = pupilcloud.LabelPostRequest() # LabelPostRequest | 

try:
    # Create a new label
    data = api.post_label(payload).result
    print(data)
except ApiException as e:
    print("Exception when calling LabelsApi->post_label: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LabelPostRequest**](LabelPostRequest.md)|  | 

### Return type

[**LabelPostResponse**](LabelPostResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created label |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

