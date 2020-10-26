# swagger_client.MerchantFulfillmentApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_shipment**](MerchantFulfillmentApi.md#cancel_shipment) | **DELETE** /mfn/v0/shipments/{shipmentId} | 
[**cancel_shipment_old**](MerchantFulfillmentApi.md#cancel_shipment_old) | **PUT** /mfn/v0/shipments/{shipmentId}/cancel | 
[**create_shipment**](MerchantFulfillmentApi.md#create_shipment) | **POST** /mfn/v0/shipments | 
[**get_additional_seller_inputs**](MerchantFulfillmentApi.md#get_additional_seller_inputs) | **POST** /mfn/v0/additionalSellerInputs | 
[**get_additional_seller_inputs_old**](MerchantFulfillmentApi.md#get_additional_seller_inputs_old) | **POST** /mfn/v0/sellerInputs | 
[**get_eligible_shipment_services**](MerchantFulfillmentApi.md#get_eligible_shipment_services) | **POST** /mfn/v0/eligibleShippingServices | 
[**get_eligible_shipment_services_old**](MerchantFulfillmentApi.md#get_eligible_shipment_services_old) | **POST** /mfn/v0/eligibleServices | 
[**get_shipment**](MerchantFulfillmentApi.md#get_shipment) | **GET** /mfn/v0/shipments/{shipmentId} | 

# **cancel_shipment**
> cancel_shipment()



Cancel the shipment indicated by the specified shipment identifier.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()
 = swagger_client.null() #  | The Amazon-defined shipment identifier for the shipment to cancel.

try:
    api_instance.cancel_shipment()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->cancel_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The Amazon-defined shipment identifier for the shipment to cancel. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_shipment_old**
> cancel_shipment_old()



Cancel the shipment indicated by the specified shipment identifer.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()
 = swagger_client.null() #  | The Amazon-defined shipment identifier for the shipment to cancel.

try:
    api_instance.cancel_shipment_old()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->cancel_shipment_old: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The Amazon-defined shipment identifier for the shipment to cancel. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shipment**
> create_shipment()



Create a shipment with the information provided.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()

try:
    api_instance.create_shipment()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->create_shipment: %s\n" % e)
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

# **get_additional_seller_inputs**
> get_additional_seller_inputs()



Gets a list of additional seller inputs required for a ship method. This is generally used for international shipping.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()

try:
    api_instance.get_additional_seller_inputs()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->get_additional_seller_inputs: %s\n" % e)
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

# **get_additional_seller_inputs_old**
> get_additional_seller_inputs_old()



Get a list of additional seller inputs required for a ship method. This is generally used for international shipping.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()

try:
    api_instance.get_additional_seller_inputs_old()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->get_additional_seller_inputs_old: %s\n" % e)
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

# **get_eligible_shipment_services**
> get_eligible_shipment_services()



Returns a list of shipping service offers that satisfy the specified shipment request details.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()

try:
    api_instance.get_eligible_shipment_services()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->get_eligible_shipment_services: %s\n" % e)
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

# **get_eligible_shipment_services_old**
> get_eligible_shipment_services_old()



Returns a list of shipping service offers that satisfy the specified shipment request details.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()

try:
    api_instance.get_eligible_shipment_services_old()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->get_eligible_shipment_services_old: %s\n" % e)
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

# **get_shipment**
> get_shipment()



Returns the shipment information for an existing shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MerchantFulfillmentApi()
 = swagger_client.null() #  | The Amazon-defined shipment identifier for the shipment.

try:
    api_instance.get_shipment()
except ApiException as e:
    print("Exception when calling MerchantFulfillmentApi->get_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The Amazon-defined shipment identifier for the shipment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

