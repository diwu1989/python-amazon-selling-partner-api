# amazon_selling_partner_api.CatalogApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_item**](CatalogApi.md#get_catalog_item) | **GET** /catalog/v0/items/{asin} | 
[**list_catalog_categories**](CatalogApi.md#list_catalog_categories) | **GET** /catalog/v0/categories | 
[**list_catalog_items**](CatalogApi.md#list_catalog_items) | **GET** /catalog/v0/items | 

# **get_catalog_item**
> get_catalog_item(, )



Returns a specified item and its attributes.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.CatalogApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for the item.
 = amazon_selling_partner_api.null() #  | The Amazon Standard Identification Number (ASIN) of the item.

try:
    api_instance.get_catalog_item(, )
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for the item. | 
 **** | [****](.md)| The Amazon Standard Identification Number (ASIN) of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog_categories**
> list_catalog_categories(, =, =)



Returns the parent categories to which an item belongs, based on the specified ASIN or SellerSKU.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.CatalogApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for the item.
 = amazon_selling_partner_api.null() #  | The Amazon Standard Identification Number (ASIN) of the item. (optional)
 = amazon_selling_partner_api.null() #  | Used to identify items in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit. (optional)

try:
    api_instance.list_catalog_categories(, =, =)
except ApiException as e:
    print("Exception when calling CatalogApi->list_catalog_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for the item. | 
 **** | [****](.md)| The Amazon Standard Identification Number (ASIN) of the item. | [optional] 
 **** | [****](.md)| Used to identify items in the given marketplace. SellerSKU is qualified by the seller&#x27;s SellerId, which is included with every operation that you submit. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_catalog_items**
> list_catalog_items(, =, =, =, =, =, =, =)



Returns a list of items and their attributes, based on a search query or item identifiers that you specify. When based on a search query, provide the Query parameter and optionally, the QueryContextId parameter. When based on item identifiers, provide a single appropriate parameter based on the identifier type, and specify the associated item value. MarketplaceId is always required.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.CatalogApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace for which items are returned.
 = amazon_selling_partner_api.null() #  | Keyword(s) to use to search for items in the catalog. Example: 'harry potter books'. (optional)
 = amazon_selling_partner_api.null() #  | An identifier for the context within which the given search will be performed. A marketplace might provide mechanisms for constraining a search to a subset of potential items. For example, the retail marketplace allows queries to be constrained to a specific category. The QueryContextId parameter specifies such a subset. If it is omitted, the search will be performed using the default context for the marketplace, which will typically contain the largest set of items. (optional)
 = amazon_selling_partner_api.null() #  | Used to identify an item in the given marketplace. SellerSKU is qualified by the seller's SellerId, which is included with every operation that you submit. (optional)
 = amazon_selling_partner_api.null() #  | A 12-digit bar code used for retail packaging. (optional)
 = amazon_selling_partner_api.null() #  | A European article number that uniquely identifies the catalog item, manufacturer, and its attributes. (optional)
 = amazon_selling_partner_api.null() #  | The unique commercial book identifier used to identify books internationally. (optional)
 = amazon_selling_partner_api.null() #  | A Japanese article number that uniquely identifies the product, manufacturer, and its attributes. (optional)

try:
    api_instance.list_catalog_items(, =, =, =, =, =, =, =)
except ApiException as e:
    print("Exception when calling CatalogApi->list_catalog_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace for which items are returned. | 
 **** | [****](.md)| Keyword(s) to use to search for items in the catalog. Example: &#x27;harry potter books&#x27;. | [optional] 
 **** | [****](.md)| An identifier for the context within which the given search will be performed. A marketplace might provide mechanisms for constraining a search to a subset of potential items. For example, the retail marketplace allows queries to be constrained to a specific category. The QueryContextId parameter specifies such a subset. If it is omitted, the search will be performed using the default context for the marketplace, which will typically contain the largest set of items. | [optional] 
 **** | [****](.md)| Used to identify an item in the given marketplace. SellerSKU is qualified by the seller&#x27;s SellerId, which is included with every operation that you submit. | [optional] 
 **** | [****](.md)| A 12-digit bar code used for retail packaging. | [optional] 
 **** | [****](.md)| A European article number that uniquely identifies the catalog item, manufacturer, and its attributes. | [optional] 
 **** | [****](.md)| The unique commercial book identifier used to identify books internationally. | [optional] 
 **** | [****](.md)| A Japanese article number that uniquely identifies the product, manufacturer, and its attributes. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

