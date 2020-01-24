# pupilcloud.AuthApi

All URIs are relative to *https://api.cloud.pupil-labs.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_profile**](AuthApi.md#get_profile) | **GET** /auth/profile | Returns the current logged in user based on auth token


# **get_profile**
> ProfileGetResponse get_profile()

Returns the current logged in user based on auth token

### Example

```python
from pupilcloud import Api, ApiException

api = pupilcloud.Api(api_key="API_KEY", host="https://api.cloud.pupil-labs.com")

try:
    # Returns the current logged in user based on auth token
    data = api.get_profile().result
    print(data)
except ApiException as e:
    print("Exception when calling AuthApi->get_profile: %s\n" % e)


```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ProfileGetResponse**](ProfileGetResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user |  -  |
**401** | Unauthorized / invalid credentials / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

