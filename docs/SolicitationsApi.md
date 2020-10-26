# amazon_selling_partner_api.SolicitationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product_review_and_seller_feedback_solicitation**](SolicitationsApi.md#create_product_review_and_seller_feedback_solicitation) | **POST** /solicitations/v1/orders/{amazonOrderId}/solicitations/productReviewAndSellerFeedback | 
[**get_solicitation_actions_for_order**](SolicitationsApi.md#get_solicitation_actions_for_order) | **GET** /solicitations/v1/orders/{amazonOrderId} | 

# **create_product_review_and_seller_feedback_solicitation**
> create_product_review_and_seller_feedback_solicitation(, )



Sends a solicitation to a buyer asking for seller feedback and a product review for the specified order. Send only one productReviewAndSellerFeedback or free form proactive message per order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SolicitationsApi()
 = amazon_selling_partner_api.null() #  | An Amazon order identifier. This specifies the order for which a solicitation is sent.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.create_product_review_and_seller_feedback_solicitation(, )
except ApiException as e:
    print("Exception when calling SolicitationsApi->create_product_review_and_seller_feedback_solicitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which a solicitation is sent. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solicitation_actions_for_order**
> get_solicitation_actions_for_order(, )



Returns a list of solicitation types that are available for an order that you specify. A solicitation type is represented by an actions object, which contains a path and query parameter(s). You can use the path and parameter(s) to call an operation that sends a solicitation. Currently only the productReviewAndSellerFeedbackSolicitation solicitation type is available.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SolicitationsApi()
 = amazon_selling_partner_api.null() #  | An Amazon order identifier. This specifies the order for which you want a list of available solicitation types.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified.

try:
    api_instance.get_solicitation_actions_for_order(, )
except ApiException as e:
    print("Exception when calling SolicitationsApi->get_solicitation_actions_for_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon order identifier. This specifies the order for which you want a list of available solicitation types. | 
 **** | [****](.md)| A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

