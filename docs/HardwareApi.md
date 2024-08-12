# pupilcloud.HardwareApi

All URIs are relative to *https://api.cloud.pupil-labs.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hardware**](HardwareApi.md#get_hardware) | **GET** /hardware/{serial_number}/calibration.{version} | Returns calibration


# **get_hardware**
> bytearray get_hardware(serial_number, version, var_json=var_json)

Returns calibration

{version} data for hardware with {serial_number}

### Example


```python
import pupilcloud
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
    api_instance = pupilcloud.HardwareApi(api_client)
    serial_number = 'serial_number_example' # str | 
    version = 'version_example' # str | 
    var_json = 'var_json_example' # str | Specify to get result in json format (optional)

    try:
        # Returns calibration
        api_response = await api_instance.get_hardware(serial_number, version, var_json=var_json)
        print("The response of HardwareApi->get_hardware:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HardwareApi->get_hardware: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 
 **version** | **str**|  | 
 **var_json** | **str**| Specify to get result in json format | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hardware data |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

