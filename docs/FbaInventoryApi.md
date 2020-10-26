# amazon_selling_partner_api.FbaInventoryApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_summaries**](FbaInventoryApi.md#get_inventory_summaries) | **GET** /fba/inventory/v1/summaries | 

# **get_inventory_summaries**
> get_inventory_summaries(, , , =, =, =, =)



Returns a list of inventory summaries. The summaries returned depend on the presence or absence of the startDateTime and sellerSkus parameters:  - All inventory summaries with available details are returned when the startDateTime and sellerSkus parameters are omitted. - When startDateTime is provided, the operation returns inventory summaries that have had changes after the date and time specified. The sellerSkus parameter is ignored. - When the sellerSkus parameter is provided, the operation returns inventory summaries for only the specified sellerSkus.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 90 | 150 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInventoryApi()
 = amazon_selling_partner_api.null() #  | The granularity type for the inventory aggregation level.
 = amazon_selling_partner_api.null() #  | The granularity ID for the inventory aggregation level.
 = amazon_selling_partner_api.null() #  | The marketplace ID for the marketplace for which to return inventory summaries.
 = amazon_selling_partner_api.null() #  | true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value). (optional)
 = amazon_selling_partner_api.null() #  | A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected. (optional)
 = amazon_selling_partner_api.null() #  | A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs. (optional)
 = amazon_selling_partner_api.null() #  | String token returned in the response of your previous request. (optional)

try:
    api_instance.get_inventory_summaries(, , , =, =, =, =)
except ApiException as e:
    print("Exception when calling FbaInventoryApi->get_inventory_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The granularity type for the inventory aggregation level. | 
 **** | [****](.md)| The granularity ID for the inventory aggregation level. | 
 **** | [****](.md)| The marketplace ID for the marketplace for which to return inventory summaries. | 
 **** | [****](.md)| true to return inventory summaries with additional summarized inventory details and quantities. Otherwise, returns inventory summaries only (default value). | [optional] 
 **** | [****](.md)| A start date and time in ISO8601 format. If specified, all inventory summaries that have changed since then are returned. You must specify a date and time that is no earlier than 18 months prior to the date and time when you call the API. Note: Changes in inboundWorkingQuantity, inboundShippedQuantity and inboundReceivingQuantity are not detected. | [optional] 
 **** | [****](.md)| A list of seller SKUs for which to return inventory summaries. You may specify up to 50 SKUs. | [optional] 
 **** | [****](.md)| String token returned in the response of your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

