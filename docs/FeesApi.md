# amazon_selling_partner_api.FeesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_fees_estimate_for_asin**](FeesApi.md#get_my_fees_estimate_for_asin) | **POST** /products/fees/v0/items/{Asin}/feesEstimate | 
[**get_my_fees_estimate_for_sku**](FeesApi.md#get_my_fees_estimate_for_sku) | **POST** /products/fees/v0/listings/{SellerSKU}/feesEstimate | 

# **get_my_fees_estimate_for_asin**
> get_my_fees_estimate_for_asin()



Returns the estimated fees for the item indicated by the specified Asin in the marketplace specified in the request body.  You can call getMyFeesEstimateForASIN for an item on behalf of a seller before the seller sets the item's price. They can then take estimated fees into account. With each product fees request, you must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FeesApi()
 = amazon_selling_partner_api.null() #  | The Amazon Standard Identification Number (ASIN) of the item.

try:
    api_instance.get_my_fees_estimate_for_asin()
except ApiException as e:
    print("Exception when calling FeesApi->get_my_fees_estimate_for_asin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The Amazon Standard Identification Number (ASIN) of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_fees_estimate_for_sku**
> get_my_fees_estimate_for_sku()



Returns the estimated fees for the item indicated by the specified seller SKU in the marketplace specified in the request body.  You can call getMyFeesEstimateForSKU for an item on behalf of a seller before the seller sets the item's price. They can then take estimated fees into account. With each fees estimate request, you must include an original identifier. This identifier is included in the fees estimate so you can correlate a fees estimate with the original request.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FeesApi()
 = amazon_selling_partner_api.null() #  | Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.

try:
    api_instance.get_my_fees_estimate_for_sku()
except ApiException as e:
    print("Exception when calling FeesApi->get_my_fees_estimate_for_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| Used to identify an item in the given marketplace. SellerSKU is qualified by the seller&#x27;s SellerId, which is included with every operation that you submit. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

