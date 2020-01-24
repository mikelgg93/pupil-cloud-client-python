# pupilcloud.TemplatesApi

All URIs are relative to *https://api.cloud.pupil-labs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template**](TemplatesApi.md#delete_template) | **DELETE** /templates/{template_id} | Delete a template
[**get_template**](TemplatesApi.md#get_template) | **GET** /templates/{template_id} | Returns a template with {template_id}
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /templates/ | List all templates
[**patch_template**](TemplatesApi.md#patch_template) | **PATCH** /templates/{template_id} | Update a template
[**post_template**](TemplatesApi.md#post_template) | **POST** /templates/ | Create a new template


# **delete_template**
> TemplateDeleteResponse delete_template(template_id)

Delete a template

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
template_id = 'template_id_example' # str | 

try:
    # Delete a template
    data = api.delete_template(template_id).result
    print(data)
except ApiException as e:
    print("Exception when calling TemplatesApi->delete_template: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**TemplateDeleteResponse**](TemplateDeleteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Delete a single template |  -  |
**401** | Authentication is required |  -  |
**405** | Method not accepted eg. trying to delete default template |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> TemplateGetResponse get_template(template_id)

Returns a template with {template_id}

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
template_id = 'template_id_example' # str | 

try:
    # Returns a template with {template_id}
    data = api.get_template(template_id).result
    print(data)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_template: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**TemplateGetResponse**](TemplateGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single template |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> TemplatesGetResponse get_templates()

List all templates

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")

try:
    # List all templates
    data = api.get_templates().result
    print(data)
except ApiException as e:
    print("Exception when calling TemplatesApi->get_templates: %s\n" % e)


```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TemplatesGetResponse**](TemplatesGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of templates |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_template**
> TemplatePatchResponse patch_template(template_id, payload)

Update a template

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
template_id = 'template_id_example' # str | 
payload = pupilcloud.TemplatePatchRequest() # TemplatePatchRequest | 

try:
    # Update a template
    data = api.patch_template(template_id, payload).result
    print(data)
except ApiException as e:
    print("Exception when calling TemplatesApi->patch_template: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **payload** | [**TemplatePatchRequest**](TemplatePatchRequest.md)|  | 

### Return type

[**TemplatePatchResponse**](TemplatePatchResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated template |  -  |
**400** | Invalid input |  -  |
**401** | Authentication is required |  -  |
**409** | Conflict |  -  |
**412** | Precondition failed, eg. If-Unmodified-Since too old |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_template**
> TemplatePostResponse post_template(payload)

Create a new template

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")
payload = pupilcloud.TemplatePostRequest() # TemplatePostRequest | 

try:
    # Create a new template
    data = api.post_template(payload).result
    print(data)
except ApiException as e:
    print("Exception when calling TemplatesApi->post_template: %s\n" % e)


```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TemplatePostRequest**](TemplatePostRequest.md)|  | 

### Return type

[**TemplatePostResponse**](TemplatePostResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created template |  -  |
**201** | Successful operation |  -  |
**401** | Authentication is required |  -  |
**409** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

