# swagger_client.NotificationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_destination**](NotificationsApi.md#create_destination) | **POST** /notifications/v1/destinations | 
[**create_subscription**](NotificationsApi.md#create_subscription) | **POST** /notifications/v1/subscriptions/{notificationType} | 
[**delete_destination**](NotificationsApi.md#delete_destination) | **DELETE** /notifications/v1/destinations/{destinationId} | 
[**delete_subscription_by_id**](NotificationsApi.md#delete_subscription_by_id) | **DELETE** /notifications/v1/subscriptions/{notificationType}/{subscriptionId} | 
[**get_destination**](NotificationsApi.md#get_destination) | **GET** /notifications/v1/destinations/{destinationId} | 
[**get_destinations**](NotificationsApi.md#get_destinations) | **GET** /notifications/v1/destinations | 
[**get_subscription**](NotificationsApi.md#get_subscription) | **GET** /notifications/v1/subscriptions/{notificationType} | 
[**get_subscription_by_id**](NotificationsApi.md#get_subscription_by_id) | **GET** /notifications/v1/subscriptions/{notificationType}/{subscriptionId} | 

# **create_destination**
> create_destination()



Creates a destination resource to receive notifications. The createDestination API is grantless. For more information, see \"Grantless operations\" in the Selling Partner API Developer Guide.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()

try:
    api_instance.create_destination()
except ApiException as e:
    print("Exception when calling NotificationsApi->create_destination: %s\n" % e)
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

# **create_subscription**
> create_subscription()



Creates a subscription for the specified notification type to be delivered to the specified destination. Before you can subscribe, you must first create the destination by calling the createDestination operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()

try:
    api_instance.create_subscription()
except ApiException as e:
    print("Exception when calling NotificationsApi->create_subscription: %s\n" % e)
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

# **delete_destination**
> delete_destination()



Deletes the destination that you specify. The deleteDestination API is grantless. For more information, see \"Grantless operations\" in the Selling Partner API Developer Guide.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
 = swagger_client.null() #  | The identifier for the destination that you want to delete.

try:
    api_instance.delete_destination()
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier for the destination that you want to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_by_id**
> delete_subscription_by_id()



Deletes the subscription indicated by the subscription identifier and notification type that you specify. The subscription identifier can be for any subscription associated with your application. After you successfully call this operation, notifications will stop being sent for the associated subscription. The deleteSubscriptionById API is grantless. For more information, see \"Grantless operations\" in the Selling Partner API Developer Guide.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
 = swagger_client.null() #  | The identifier for the subscription that you want to delete.

try:
    api_instance.delete_subscription_by_id()
except ApiException as e:
    print("Exception when calling NotificationsApi->delete_subscription_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier for the subscription that you want to delete. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destination**
> get_destination()



Returns information about the destination that you specify. The getDestination API is grantless. For more information, see \"Grantless operations\" in the Selling Partner API Developer Guide.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
 = swagger_client.null() #  | The identifier generated when you created the destination.

try:
    api_instance.get_destination()
except ApiException as e:
    print("Exception when calling NotificationsApi->get_destination: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier generated when you created the destination. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_destinations**
> get_destinations()



Returns information about all destinations. The getDestinations API is grantless. For more information, see \"Grantless operations\" in the Selling Partner API Developer Guide.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()

try:
    api_instance.get_destinations()
except ApiException as e:
    print("Exception when calling NotificationsApi->get_destinations: %s\n" % e)
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

# **get_subscription**
> get_subscription()



Returns information about subscriptions of the specified notification type. You can use this API to get subscription information when you do not have a subscription identifier.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()

try:
    api_instance.get_subscription()
except ApiException as e:
    print("Exception when calling NotificationsApi->get_subscription: %s\n" % e)
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

# **get_subscription_by_id**
> get_subscription_by_id()



Returns information about a subscription for the specified notification type. The getSubscriptionById API is grantless. For more information, see \"Grantless operations\" in the Selling Partner API Developer Guide.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationsApi()
 = swagger_client.null() #  | The identifier for the subscription that you want to get.

try:
    api_instance.get_subscription_by_id()
except ApiException as e:
    print("Exception when calling NotificationsApi->get_subscription_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier for the subscription that you want to get. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

