# amazon_selling_partner_api.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_financial_event_groups**](DefaultApi.md#list_financial_event_groups) | **GET** /finances/v0/financialEventGroups | 
[**list_financial_events**](DefaultApi.md#list_financial_events) | **GET** /finances/v0/financialEvents | 
[**list_financial_events_by_group_id**](DefaultApi.md#list_financial_events_by_group_id) | **GET** /finances/v0/financialEventGroups/{eventGroupId}/financialEvents | 
[**list_financial_events_by_order_id**](DefaultApi.md#list_financial_events_by_order_id) | **GET** /finances/v0/orders/{orderId}/financialEvents | 

# **list_financial_event_groups**
> list_financial_event_groups(=, =, =, =)



Returns financial event groups for a given date range.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.DefaultApi()
 = amazon_selling_partner_api.null() #  | The maximum number of results to return per page. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting financial event groups that opened before (but not at) a specified date and time, in ISO 8601 format. The date-time  must be later than FinancialEventGroupStartedAfter and no later than two minutes before the request was submitted. If FinancialEventGroupStartedAfter and FinancialEventGroupStartedBefore are more than 180 days apart, no financial event groups are returned. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting financial event groups that opened after (or at) a specified date and time, in ISO 8601 format. The date-time must be no later than two minutes before the request was submitted. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response of your previous request. (optional)

try:
    api_instance.list_financial_event_groups(=, =, =, =)
except ApiException as e:
    print("Exception when calling DefaultApi->list_financial_event_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The maximum number of results to return per page. | [optional] 
 **** | [****](.md)| A date used for selecting financial event groups that opened before (but not at) a specified date and time, in ISO 8601 format. The date-time  must be later than FinancialEventGroupStartedAfter and no later than two minutes before the request was submitted. If FinancialEventGroupStartedAfter and FinancialEventGroupStartedBefore are more than 180 days apart, no financial event groups are returned. | [optional] 
 **** | [****](.md)| A date used for selecting financial event groups that opened after (or at) a specified date and time, in ISO 8601 format. The date-time must be no later than two minutes before the request was submitted. | [optional] 
 **** | [****](.md)| A string token returned in the response of your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_financial_events**
> list_financial_events(=, =, =, =)



Returns financial events for the specified data range.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.DefaultApi()
 = amazon_selling_partner_api.null() #  | The maximum number of results to return per page. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting financial events posted after (or at) a specified time. The date-time must be no later than two minutes before the request was submitted, in ISO 8601 date time format. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting financial events posted before (but not at) a specified time. The date-time must be later than PostedAfter and no later than two minutes before the request was submitted, in ISO 8601 date time format. If PostedAfter and PostedBefore are more than 180 days apart, no financial events are returned. You must specify the PostedAfter parameter if you specify the PostedBefore parameter. Default: Now minus two minutes. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response of your previous request. (optional)

try:
    api_instance.list_financial_events(=, =, =, =)
except ApiException as e:
    print("Exception when calling DefaultApi->list_financial_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The maximum number of results to return per page. | [optional] 
 **** | [****](.md)| A date used for selecting financial events posted after (or at) a specified time. The date-time must be no later than two minutes before the request was submitted, in ISO 8601 date time format. | [optional] 
 **** | [****](.md)| A date used for selecting financial events posted before (but not at) a specified time. The date-time must be later than PostedAfter and no later than two minutes before the request was submitted, in ISO 8601 date time format. If PostedAfter and PostedBefore are more than 180 days apart, no financial events are returned. You must specify the PostedAfter parameter if you specify the PostedBefore parameter. Default: Now minus two minutes. | [optional] 
 **** | [****](.md)| A string token returned in the response of your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_financial_events_by_group_id**
> list_financial_events_by_group_id(, =, =)



Returns all financial events for the specified financial event group.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.DefaultApi()
 = amazon_selling_partner_api.null() #  | The identifier of the financial event group to which the events belong.
 = amazon_selling_partner_api.null() #  | The maximum number of results to return per page. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response of your previous request. (optional)

try:
    api_instance.list_financial_events_by_group_id(, =, =)
except ApiException as e:
    print("Exception when calling DefaultApi->list_financial_events_by_group_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The identifier of the financial event group to which the events belong. | 
 **** | [****](.md)| The maximum number of results to return per page. | [optional] 
 **** | [****](.md)| A string token returned in the response of your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_financial_events_by_order_id**
> list_financial_events_by_order_id(, =, =)



Returns all financial events for the specified order.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 0.5 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.DefaultApi()
 = amazon_selling_partner_api.null() #  | An Amazon-defined order identifier, in 3-7-7 format.
 = amazon_selling_partner_api.null() #  | The maximum number of results to return per page. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response of your previous request. (optional)

try:
    api_instance.list_financial_events_by_order_id(, =, =)
except ApiException as e:
    print("Exception when calling DefaultApi->list_financial_events_by_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon-defined order identifier, in 3-7-7 format. | 
 **** | [****](.md)| The maximum number of results to return per page. | [optional] 
 **** | [****](.md)| A string token returned in the response of your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

