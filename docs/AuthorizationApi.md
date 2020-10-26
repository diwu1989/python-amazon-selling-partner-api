# swagger_client.AuthorizationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authorization_code**](AuthorizationApi.md#get_authorization_code) | **GET** /authorization/v1/authorizationCode | Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.

# **get_authorization_code**
> get_authorization_code(, , )

Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.

With the getAuthorizationCode operation, you can request a Login With Amazon (LWA) authorization code that will allow you to call a Selling Partner API on behalf of a seller who has already authorized you to call Amazon Marketplace Web Service (Amazon MWS). You specify a developer ID, an MWS auth token, and a seller ID. Taken together, these represent the Amazon MWS authorization that the seller previously granted you. The operation returns an LWA authorization code that can be exchanged for a refresh token and access token representing authorization to call the Selling Partner API on the seller's behalf. By using this API, sellers who have already authorized you for Amazon MWS do not need to re-authorize you for the Selling Partner API.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi()
 = swagger_client.null() #  | The seller ID of the seller for whom you are requesting Selling Partner API authorization. This must be the seller ID of the seller who authorized your application on the Marketplace Appstore.
 = swagger_client.null() #  | Your developer ID. This must be one of the developer ID values that you provided when you registered your application in Developer Central.
 = swagger_client.null() #  | The MWS Auth Token that was generated when the seller authorized your application on the Marketplace Appstore.

try:
    # Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.
    api_instance.get_authorization_code(, , )
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The seller ID of the seller for whom you are requesting Selling Partner API authorization. This must be the seller ID of the seller who authorized your application on the Marketplace Appstore. | 
 **** | [****](.md)| Your developer ID. This must be one of the developer ID values that you provided when you registered your application in Developer Central. | 
 **** | [****](.md)| The MWS Auth Token that was generated when the seller authorized your application on the Marketplace Appstore. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

