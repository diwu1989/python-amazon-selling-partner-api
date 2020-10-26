# swagger_client.MessagingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_customization_details**](MessagingApi.md#confirm_customization_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails | 
[**create_amazon_motors**](MessagingApi.md#create_amazon_motors) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/amazonMotors | 
[**create_confirm_delivery_details**](MessagingApi.md#create_confirm_delivery_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails | 
[**create_confirm_order_details**](MessagingApi.md#create_confirm_order_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails | 
[**create_confirm_service_details**](MessagingApi.md#create_confirm_service_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails | 
[**create_digital_access_key**](MessagingApi.md#create_digital_access_key) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey | 
[**create_legal_disclosure**](MessagingApi.md#create_legal_disclosure) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure | 
[**create_negative_feedback_removal**](MessagingApi.md#create_negative_feedback_removal) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/negativeFeedbackRemoval | 
[**create_unexpected_problem**](MessagingApi.md#create_unexpected_problem) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem | 
[**create_warranty**](MessagingApi.md#create_warranty) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/warranty | 
[**get_attributes**](MessagingApi.md#get_attributes) | **GET** /messaging/v1/orders/{amazonOrderId}/attributes | 
[**get_messaging_actions_for_order**](MessagingApi.md#get_messaging_actions_for_order) | **GET** /messaging/v1/orders/{amazonOrderId} | 

# **confirm_customization_details**
> confirm_customization_details(, )



Sends a message asking a buyer to provide or verify customization details such as name spelling, images, initials, etc.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.confirm_customization_details(, )
except ApiException as e:
    print("Exception when calling MessagingApi->confirm_customization_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_amazon_motors**
> create_amazon_motors(, )



Sends a message to a buyer to provide details about an Amazon Motors order. This message can only be sent by Amazon Motors sellers.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_amazon_motors(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_amazon_motors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_confirm_delivery_details**
> create_confirm_delivery_details(, )



Sends a message to a buyer to arrange a delivery or to confirm contact information for making a delivery.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_confirm_delivery_details(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_confirm_delivery_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_confirm_order_details**
> create_confirm_order_details(, )



Sends a message to ask a buyer an order-related question prior to shipping their order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_confirm_order_details(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_confirm_order_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_confirm_service_details**
> create_confirm_service_details(, )



Sends a message to contact a Home Service customer to arrange a service call or to gather information prior to a service call.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_confirm_service_details(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_confirm_service_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_digital_access_key**
> create_digital_access_key(, )



Sends a message to a buyer to share a digital access key needed to utilize digital content in their order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_digital_access_key(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_digital_access_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_legal_disclosure**
> create_legal_disclosure(, )



Sends a critical message that contains documents that a seller is legally obligated to provide to the buyer. This message should only be used to deliver documents that are required by law.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_legal_disclosure(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_legal_disclosure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_negative_feedback_removal**
> create_negative_feedback_removal(, )



Sends a non-critical message that asks a buyer to remove their negative feedback. This message should only be sent after the seller has resolved the buyer's problem.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_negative_feedback_removal(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_negative_feedback_removal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_unexpected_problem**
> create_unexpected_problem(, )



Sends a critical message to a buyer that an unexpected problem was encountered affecting the completion of the order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_unexpected_problem(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_unexpected_problem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_warranty**
> create_warranty(, )



Sends a message to a buyer to provide details about warranty information on a purchase in their order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_warranty(, )
except ApiException as e:
    print("Exception when calling MessagingApi->create_warranty: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> get_attributes(, )



Returns a response containing attributes related to an order. This includes buyer preferences.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which a message is sent.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.get_attributes(, )
except ApiException as e:
    print("Exception when calling MessagingApi->get_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a message is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_actions_for_order**
> get_messaging_actions_for_order(, )



Returns a list of message types that are available for an order that you specify. A message type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a message.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MessagingApi()
 = swagger_client.null() #  | An Amazon order identifier. This specifies the order for which you want a list of available message types.
 = swagger_client.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.get_messaging_actions_for_order(, )
except ApiException as e:
    print("Exception when calling MessagingApi->get_messaging_actions_for_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which you want a list of available message types. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

