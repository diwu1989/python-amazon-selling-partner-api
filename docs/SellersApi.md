# swagger_client.SellersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_marketplace_participations**](SellersApi.md#get_marketplace_participations) | **GET** /sellers/v1/marketplaceParticipations | 

# **get_marketplace_participations**
> get_marketplace_participations()



Returns a list of marketplaces that the seller submitting the request can sell in and information about the seller's participation in those marketplaces.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | .016 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SellersApi()

try:
    api_instance.get_marketplace_participations()
except ApiException as e:
    print("Exception when calling SellersApi->get_marketplace_participations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

