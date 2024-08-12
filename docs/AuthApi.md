# pupilcloud.AuthApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_token**](AuthApi.md#delete_token) | **DELETE** /auth/tokens/{token_id} | Delete an access token
[**delete_workspace_invitation**](AuthApi.md#delete_workspace_invitation) | **DELETE** /auth/profile/invites/{token} | Delete a workspace invitation
[**get_canny_sso_token**](AuthApi.md#get_canny_sso_token) | **GET** /auth/canny-sso | Returns the canny
[**get_profile**](AuthApi.md#get_profile) | **GET** /auth/profile | Returns the current logged in user based on auth token
[**get_token**](AuthApi.md#get_token) | **GET** /auth/tokens/{token_id} | Get an access token
[**get_tokens**](AuthApi.md#get_tokens) | **GET** /auth/tokens | Get all access tokens
[**get_workspace_invitation**](AuthApi.md#get_workspace_invitation) | **GET** /auth/profile/invites/{token} | get workspace inviation for token
[**get_workspace_invitations**](AuthApi.md#get_workspace_invitations) | **GET** /auth/profile/invites | List all workspace inviations for current user
[**patch_profile**](AuthApi.md#patch_profile) | **PATCH** /auth/profile | Update user profile
[**post_accept_invitation_resource**](AuthApi.md#post_accept_invitation_resource) | **POST** /auth/profile/invites/{token}/accept | Create workspace member based on invite token
[**post_login**](AuthApi.md#post_login) | **POST** /auth/login | Login the user and return a new session cookie
[**post_logout**](AuthApi.md#post_logout) | **POST** /auth/logout | Logout the current user
[**post_token**](AuthApi.md#post_token) | **POST** /auth/tokens | Creates a new access token
[**post_unregister**](AuthApi.md#post_unregister) | **POST** /auth/unregister | Unregisters the currently logged in user


# **delete_token**
> TokenDeleteResponse delete_token(token_id)

Delete an access token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.token_delete_response import TokenDeleteResponse
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
    api_instance = pupilcloud.AuthApi(api_client)
    token_id = 'token_id_example' # str | 

    try:
        # Delete an access token
        api_response = await api_instance.delete_token(token_id)
        print("The response of AuthApi->delete_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->delete_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

[**TokenDeleteResponse**](TokenDeleteResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_workspace_invitation**
> delete_workspace_invitation(token)

Delete a workspace invitation

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
    api_instance = pupilcloud.AuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # Delete a workspace invitation
        await api_instance.delete_workspace_invitation(token)
    except Exception as e:
        print("Exception when calling AuthApi->delete_workspace_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_canny_sso_token**
> CannySsoTokenGetResponse get_canny_sso_token()

Returns the canny

io SSO token for current user

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.canny_sso_token_get_response import CannySsoTokenGetResponse
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
    api_instance = pupilcloud.AuthApi(api_client)

    try:
        # Returns the canny
        api_response = await api_instance.get_canny_sso_token()
        print("The response of AuthApi->get_canny_sso_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_canny_sso_token: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CannySsoTokenGetResponse**](CannySsoTokenGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Canny sso token |  -  |
**401** | Unauthorized / invalid credentials / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile**
> ProfileGetResponse get_profile()

Returns the current logged in user based on auth token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.profile_get_response import ProfileGetResponse
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
    api_instance = pupilcloud.AuthApi(api_client)

    try:
        # Returns the current logged in user based on auth token
        api_response = await api_instance.get_profile()
        print("The response of AuthApi->get_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ProfileGetResponse**](ProfileGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user |  -  |
**401** | Unauthorized / invalid credentials / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> TokenGetResponse get_token(token_id)

Get an access token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.token_get_response import TokenGetResponse
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
    api_instance = pupilcloud.AuthApi(api_client)
    token_id = 'token_id_example' # str | 

    try:
        # Get an access token
        api_response = await api_instance.get_token(token_id)
        print("The response of AuthApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

[**TokenGetResponse**](TokenGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> TokensGetResponse get_tokens()

Get all access tokens

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.tokens_get_response import TokensGetResponse
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
    api_instance = pupilcloud.AuthApi(api_client)

    try:
        # Get all access tokens
        api_response = await api_instance.get_tokens()
        print("The response of AuthApi->get_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_tokens: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TokensGetResponse**](TokensGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_invitation**
> WorkspaceInvitationGetResponse get_workspace_invitation(token)

get workspace inviation for token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitation_get_response import WorkspaceInvitationGetResponse
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
    api_instance = pupilcloud.AuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # get workspace inviation for token
        api_response = await api_instance.get_workspace_invitation(token)
        print("The response of AuthApi->get_workspace_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_workspace_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**WorkspaceInvitationGetResponse**](WorkspaceInvitationGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitation |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_invitations**
> WorkspaceInvitationsGetResponse get_workspace_invitations()

List all workspace inviations for current user

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.workspace_invitations_get_response import WorkspaceInvitationsGetResponse
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
    api_instance = pupilcloud.AuthApi(api_client)

    try:
        # List all workspace inviations for current user
        api_response = await api_instance.get_workspace_invitations()
        print("The response of AuthApi->get_workspace_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_workspace_invitations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WorkspaceInvitationsGetResponse**](WorkspaceInvitationsGetResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace invitations |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_profile**
> ProfilePatchResponse patch_profile(payload)

Update user profile

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.profile_patch_request import ProfilePatchRequest
from pupilcloud.models.profile_patch_response import ProfilePatchResponse
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
    api_instance = pupilcloud.AuthApi(api_client)
    payload = pupilcloud.ProfilePatchRequest() # ProfilePatchRequest | 

    try:
        # Update user profile
        api_response = await api_instance.patch_profile(payload)
        print("The response of AuthApi->patch_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->patch_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ProfilePatchRequest**](ProfilePatchRequest.md)|  | 

### Return type

[**ProfilePatchResponse**](ProfilePatchResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated profile |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accept_invitation_resource**
> AcceptInvitationResourcePostResponse post_accept_invitation_resource(token)

Create workspace member based on invite token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.accept_invitation_resource_post_response import AcceptInvitationResourcePostResponse
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
    api_instance = pupilcloud.AuthApi(api_client)
    token = 'token_example' # str | 

    try:
        # Create workspace member based on invite token
        api_response = await api_instance.post_accept_invitation_resource(token)
        print("The response of AuthApi->post_accept_invitation_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->post_accept_invitation_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**AcceptInvitationResourcePostResponse**](AcceptInvitationResourcePostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Workspace member |  -  |
**401** | Authentication is required |  -  |
**409** | Member already member of workspace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_login**
> LoginPostResponse post_login(payload)

Login the user and return a new session cookie

### Example


```python
import pupilcloud
from pupilcloud.models.login_post_response import LoginPostResponse
from pupilcloud.models.login_request import LoginRequest
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
    api_instance = pupilcloud.AuthApi(api_client)
    payload = pupilcloud.LoginRequest() # LoginRequest | 

    try:
        # Login the user and return a new session cookie
        api_response = await api_instance.post_login(payload)
        print("The response of AuthApi->post_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->post_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**LoginRequest**](LoginRequest.md)|  | 

### Return type

[**LoginPostResponse**](LoginPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login success |  -  |
**400** | Invalid input |  -  |
**401** | Invalid token |  -  |
**403** | Token expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_logout**
> LogoutPostResponse post_logout()

Logout the current user

### Example


```python
import pupilcloud
from pupilcloud.models.logout_post_response import LogoutPostResponse
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
    api_instance = pupilcloud.AuthApi(api_client)

    try:
        # Logout the current user
        api_response = await api_instance.post_logout()
        print("The response of AuthApi->post_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->post_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LogoutPostResponse**](LogoutPostResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The current user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_token**
> TokenPostResponse post_token(payload)

Creates a new access token

### Example

* Api Key Authentication (workspace_id):
* Api Key Authentication (api_key):

```python
import pupilcloud
from pupilcloud.models.token_post_request import TokenPostRequest
from pupilcloud.models.token_post_response import TokenPostResponse
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
    api_instance = pupilcloud.AuthApi(api_client)
    payload = pupilcloud.TokenPostRequest() # TokenPostRequest | 

    try:
        # Creates a new access token
        api_response = await api_instance.post_token(payload)
        print("The response of AuthApi->post_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->post_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**TokenPostRequest**](TokenPostRequest.md)|  | 

### Return type

[**TokenPostResponse**](TokenPostResponse.md)

### Authorization

[workspace_id](../README.md#workspace_id), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The token response |  -  |
**401** | Authentication is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_unregister**
> post_unregister()

Unregisters the currently logged in user

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
    api_instance = pupilcloud.AuthApi(api_client)

    try:
        # Unregisters the currently logged in user
        await api_instance.post_unregister()
    except Exception as e:
        print("Exception when calling AuthApi->post_unregister: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Unregistered successully |  -  |
**401** | Unauthorized / cookie expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

