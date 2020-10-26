# amazon_selling_partner_api.SalesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_metrics**](SalesApi.md#get_order_metrics) | **GET** /sales/v1/orderMetrics | 

# **get_order_metrics**
> get_order_metrics(, , , =, =, =, =, =, =)



Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | .5 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SalesApi()
 = amazon_selling_partner_api.null() #  | A list of marketplace identifiers. Example: ATVPDKIKX0DER indicates the US marketplace.
 = amazon_selling_partner_api.null() #  | A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone.
 = amazon_selling_partner_api.null() #  | The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone.
 = amazon_selling_partner_api.null() #  | An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone. (optional)
 = amazon_selling_partner_api.null() #  | Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers. (optional)
 = amazon_selling_partner_api.null() #  | Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (Amazon fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network. (optional)
 = amazon_selling_partner_api.null() #  | Specifies the day that the week starts on when granularity=Week, either Monday or Sunday. Default: Monday. Example: Sunday, if you want the week to start on a Sunday. (optional)
 = amazon_selling_partner_api.null() #  | Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN. (optional)
 = amazon_selling_partner_api.null() #  | Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU. (optional)

try:
    api_instance.get_order_metrics(, , , =, =, =, =, =, =)
except ApiException as e:
    print("Exception when calling SalesApi->get_order_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A list of marketplace identifiers. Example: ATVPDKIKX0DER indicates the US marketplace. | 
 **** | [****](.md)| A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone. | 
 **** | [****](.md)| The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity&#x3D;Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity&#x3D;Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone. | 
 **** | [****](.md)| An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone. | [optional] 
 **** | [****](.md)| Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers. | [optional] 
 **** | [****](.md)| Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (Amazon fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network. | [optional] 
 **** | [****](.md)| Specifies the day that the week starts on when granularity&#x3D;Week, either Monday or Sunday. Default: Monday. Example: Sunday, if you want the week to start on a Sunday. | [optional] 
 **** | [****](.md)| Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN. | [optional] 
 **** | [****](.md)| Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

