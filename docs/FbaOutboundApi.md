# amazon_selling_partner_api.FbaOutboundApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_fulfillment_order**](FbaOutboundApi.md#cancel_fulfillment_order) | **PUT** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel | 
[**create_fulfillment_order**](FbaOutboundApi.md#create_fulfillment_order) | **POST** /fba/outbound/v0/fulfillmentOrders | 
[**create_fulfillment_return**](FbaOutboundApi.md#create_fulfillment_return) | **PUT** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId}/return | 
[**get_fulfillment_order**](FbaOutboundApi.md#get_fulfillment_order) | **GET** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId} | 
[**get_fulfillment_preview**](FbaOutboundApi.md#get_fulfillment_preview) | **POST** /fba/outbound/v0/fulfillmentOrders/preview | 
[**get_package_tracking_details**](FbaOutboundApi.md#get_package_tracking_details) | **GET** /fba/outbound/v0/tracking | 
[**list_all_fulfillment_orders**](FbaOutboundApi.md#list_all_fulfillment_orders) | **GET** /fba/outbound/v0/fulfillmentOrders | 
[**list_return_reason_codes**](FbaOutboundApi.md#list_return_reason_codes) | **GET** /fba/outbound/v0/returnReasonCodes | 
[**update_fulfillment_order**](FbaOutboundApi.md#update_fulfillment_order) | **PUT** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId} | 

# **cancel_fulfillment_order**
> cancel_fulfillment_order()



Requests that Amazon stop attempting to fulfill the fulfillment order indicated by the specified order identifier.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_instance.cancel_fulfillment_order()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->cancel_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fulfillment_order**
> create_fulfillment_order()



Requests that Amazon ship items from the seller's inventory in Amazon's fulfillment network to a destination address.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()

try:
    api_instance.create_fulfillment_order()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->create_fulfillment_order: %s\n" % e)
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

# **create_fulfillment_return**
> create_fulfillment_return()



Creates a fulfillment return.   **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | An identifier assigned by the seller to the fulfillment order at the time it was created. The seller uses their own records to find the correct SellerFulfillmentOrderId value based on the buyer's request to return items.

try:
    api_instance.create_fulfillment_return()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->create_fulfillment_return: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An identifier assigned by the seller to the fulfillment order at the time it was created. The seller uses their own records to find the correct SellerFulfillmentOrderId value based on the buyer&#x27;s request to return items. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_order**
> get_fulfillment_order()



Returns the fulfillment order indicated by the specified order identifier.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_instance.get_fulfillment_order()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment_preview**
> get_fulfillment_preview()



Returns a list of fulfillment order previews based on shipping criteria that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()

try:
    api_instance.get_fulfillment_preview()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_fulfillment_preview: %s\n" % e)
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

# **get_package_tracking_details**
> get_package_tracking_details()



Returns delivery tracking information for a package in an outbound shipment for a Multi-Channel Fulfillment order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | The unencrypted package identifier returned by the getFulfillmentOrder operation.

try:
    api_instance.get_package_tracking_details()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->get_package_tracking_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The unencrypted package identifier returned by the getFulfillmentOrder operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_fulfillment_orders**
> list_all_fulfillment_orders(=, =, =)



Returns a list of fulfillment orders fulfilled after (or at) a specified date-time, or indicated by the next token parameter.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | A date and time used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order. (optional)
 = amazon_selling_partner_api.null() #  | Indicates the intended recipient channel for the order. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response to your previous request. (optional)

try:
    api_instance.list_all_fulfillment_orders(=, =, =)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->list_all_fulfillment_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A date and time used to select fulfillment orders that were last updated after (or at) a specified time. An update is defined as any change in fulfillment order status, including the creation of a new fulfillment order. | [optional] 
 **** | [****](.md)| Indicates the intended recipient channel for the order. | [optional] 
 **** | [****](.md)| A string token returned in the response to your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_return_reason_codes**
> list_return_reason_codes(, , =, =)



Returns a list of return reason codes for a seller SKU in a given marketplace.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | The seller SKU for which return reason codes are required.
 = amazon_selling_partner_api.null() #  | The language that the TranslatedDescription property of the ReasonCodeDetails response object should be translated into.
 = amazon_selling_partner_api.null() #  | The marketplace for which the seller wants return reason codes. (optional)
 = amazon_selling_partner_api.null() #  | The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes. (optional)

try:
    api_instance.list_return_reason_codes(, , =, =)
except ApiException as e:
    print("Exception when calling FbaOutboundApi->list_return_reason_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The seller SKU for which return reason codes are required. | 
 **** | [****](.md)| The language that the TranslatedDescription property of the ReasonCodeDetails response object should be translated into. | 
 **** | [****](.md)| The marketplace for which the seller wants return reason codes. | [optional] 
 **** | [****](.md)| The identifier assigned to the item by the seller when the fulfillment order was created. The service uses this value to determine the marketplace for which the seller wants return reason codes. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fulfillment_order**
> update_fulfillment_order()



Updates and/or requests shipment for a fulfillment order with an order hold on it.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaOutboundApi()
 = amazon_selling_partner_api.null() #  | The identifier assigned to the item by the seller when the fulfillment order was created.

try:
    api_instance.update_fulfillment_order()
except ApiException as e:
    print("Exception when calling FbaOutboundApi->update_fulfillment_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier assigned to the item by the seller when the fulfillment order was created. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

