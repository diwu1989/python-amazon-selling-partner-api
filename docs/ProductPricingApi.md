# amazon_selling_partner_api.ProductPricingApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_competitive_pricing**](ProductPricingApi.md#get_competitive_pricing) | **GET** /products/pricing/v0/competitivePrice | 
[**get_item_offers**](ProductPricingApi.md#get_item_offers) | **GET** /products/pricing/v0/items/{Asin}/offers | 
[**get_listing_offers**](ProductPricingApi.md#get_listing_offers) | **GET** /products/pricing/v0/listings/{SellerSKU}/offers | 
[**get_pricing**](ProductPricingApi.md#get_pricing) | **GET** /products/pricing/v0/price | 

# **get_competitive_pricing**
> get_competitive_pricing(, , =, =)



Returns competitive pricing information for a seller's offer listings based on seller SKU or ASIN.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ProductPricingApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for which prices are returned.
 = amazon_selling_partner_api.null() #  | Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku.
 = amazon_selling_partner_api.null() #  | A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace. (optional)
 = amazon_selling_partner_api.null() #  | A list of up to twenty seller SKU values used to identify items in the given marketplace. (optional)

try:
    api_instance.get_competitive_pricing(, , =, =)
except ApiException as e:
    print("Exception when calling ProductPricingApi->get_competitive_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for which prices are returned. | 
 **** | [****](.md)| Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. Possible values: Asin, Sku. | 
 **** | [****](.md)| A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace. | [optional] 
 **** | [****](.md)| A list of up to twenty seller SKU values used to identify items in the given marketplace. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_offers**
> get_item_offers(, , )



Returns the lowest priced offers for a single item based on ASIN.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ProductPricingApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for which prices are returned.
 = amazon_selling_partner_api.null() #  | Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
 = amazon_selling_partner_api.null() #  | The Amazon Standard Identification Number (ASIN) of the item.

try:
    api_instance.get_item_offers(, , )
except ApiException as e:
    print("Exception when calling ProductPricingApi->get_item_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for which prices are returned. | 
 **** | [****](.md)| Filters the offer listings to be considered based on item condition. Possible values: New, Used, Collectible, Refurbished, Club. | 
 **** | [****](.md)| The Amazon Standard Identification Number (ASIN) of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_offers**
> get_listing_offers(, , )



Returns the lowest priced offers for a single SKU listing.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ProductPricingApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for which prices are returned.
 = amazon_selling_partner_api.null() #  | Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.
 = amazon_selling_partner_api.null() #  | Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit.

try:
    api_instance.get_listing_offers(, , )
except ApiException as e:
    print("Exception when calling ProductPricingApi->get_listing_offers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for which prices are returned. | 
 **** | [****](.md)| Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club. | 
 **** | [****](.md)| Identifies an item in the given marketplace. SellerSKU is qualified by the seller&#x27;s SellerId, which is included with every operation that you submit. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing**
> get_pricing(, , =, =, =)



Returns pricing information for a seller's offer listings based on seller SKU or ASIN.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ProductPricingApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for which prices are returned.
 = amazon_selling_partner_api.null() #  | Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter.
 = amazon_selling_partner_api.null() #  | A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace. (optional)
 = amazon_selling_partner_api.null() #  | A list of up to twenty seller SKU values used to identify items in the given marketplace. (optional)
 = amazon_selling_partner_api.null() #  | Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club. (optional)

try:
    api_instance.get_pricing(, , =, =, =)
except ApiException as e:
    print("Exception when calling ProductPricingApi->get_pricing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for which prices are returned. | 
 **** | [****](.md)| Indicates whether ASIN values or seller SKU values are used to identify items. If you specify Asin, the information in the response will be dependent on the list of Asins you provide in the Asins parameter. If you specify Sku, the information in the response will be dependent on the list of Skus you provide in the Skus parameter. | 
 **** | [****](.md)| A list of up to twenty Amazon Standard Identification Number (ASIN) values used to identify items in the given marketplace. | [optional] 
 **** | [****](.md)| A list of up to twenty seller SKU values used to identify items in the given marketplace. | [optional] 
 **** | [****](.md)| Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

