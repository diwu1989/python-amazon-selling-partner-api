# amazon_selling_partner_api.SmallAndLightApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_small_and_light_enrollment_by_seller_sku**](SmallAndLightApi.md#delete_small_and_light_enrollment_by_seller_sku) | **DELETE** /fba/smallAndLight/v1/enrollments/{sellerSKU} | 
[**get_small_and_light_eligibility_by_seller_sku**](SmallAndLightApi.md#get_small_and_light_eligibility_by_seller_sku) | **GET** /fba/smallAndLight/v1/eligibilities/{sellerSKU} | 
[**get_small_and_light_enrollment_by_seller_sku**](SmallAndLightApi.md#get_small_and_light_enrollment_by_seller_sku) | **GET** /fba/smallAndLight/v1/enrollments/{sellerSKU} | 
[**get_small_and_light_fee_preview**](SmallAndLightApi.md#get_small_and_light_fee_preview) | **POST** /fba/smallAndLight/v1/feePreviews | 
[**put_small_and_light_enrollment_by_seller_sku**](SmallAndLightApi.md#put_small_and_light_enrollment_by_seller_sku) | **PUT** /fba/smallAndLight/v1/enrollments/{sellerSKU} | 

# **delete_small_and_light_enrollment_by_seller_sku**
> delete_small_and_light_enrollment_by_seller_sku(, )



Removes the item indicated by the specified seller SKU from the Small and Light program in the specified marketplace. If the item is not eligible for disenrollment, the ineligibility reasons are returned.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SmallAndLightApi()
 = amazon_selling_partner_api.null() #  | The seller SKU that identifies the item.
 = amazon_selling_partner_api.null() #  | The marketplace in which to remove the item from the Small and Light program. Note: Accepts a single marketplace only.

try:
    api_instance.delete_small_and_light_enrollment_by_seller_sku(, )
except ApiException as e:
    print("Exception when calling SmallAndLightApi->delete_small_and_light_enrollment_by_seller_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The seller SKU that identifies the item. | 
 **** | [****](.md)| The marketplace in which to remove the item from the Small and Light program. Note: Accepts a single marketplace only. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_small_and_light_eligibility_by_seller_sku**
> get_small_and_light_eligibility_by_seller_sku(, )



Returns the Small and Light program eligibility status of the item indicated by the specified seller SKU in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SmallAndLightApi()
 = amazon_selling_partner_api.null() #  | The seller SKU that identifies the item.
 = amazon_selling_partner_api.null() #  | The marketplace for which the eligibility status is retrieved. NOTE: Accepts a single marketplace only.

try:
    api_instance.get_small_and_light_eligibility_by_seller_sku(, )
except ApiException as e:
    print("Exception when calling SmallAndLightApi->get_small_and_light_eligibility_by_seller_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The seller SKU that identifies the item. | 
 **** | [****](.md)| The marketplace for which the eligibility status is retrieved. NOTE: Accepts a single marketplace only. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_small_and_light_enrollment_by_seller_sku**
> get_small_and_light_enrollment_by_seller_sku(, )



Returns the Small and Light enrollment status for the item indicated by the specified seller SKU in the specified marketplace.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 10 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SmallAndLightApi()
 = amazon_selling_partner_api.null() #  | The seller SKU that identifies the item.
 = amazon_selling_partner_api.null() #  | The marketplace for which the enrollment status is retrieved. Note: Accepts a single marketplace only.

try:
    api_instance.get_small_and_light_enrollment_by_seller_sku(, )
except ApiException as e:
    print("Exception when calling SmallAndLightApi->get_small_and_light_enrollment_by_seller_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The seller SKU that identifies the item. | 
 **** | [****](.md)| The marketplace for which the enrollment status is retrieved. Note: Accepts a single marketplace only. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_small_and_light_fee_preview**
> get_small_and_light_fee_preview()



Returns the Small and Light fee estimates for the specified items. You must include a marketplaceId parameter to retrieve the proper fee estimates for items to be sold in that marketplace. The ordering of items in the response will mirror the order of the items in the request. Duplicate ASIN/price combinations are removed.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 3 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SmallAndLightApi()

try:
    api_instance.get_small_and_light_fee_preview()
except ApiException as e:
    print("Exception when calling SmallAndLightApi->get_small_and_light_fee_preview: %s\n" % e)
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

# **put_small_and_light_enrollment_by_seller_sku**
> put_small_and_light_enrollment_by_seller_sku(, )



Enrolls the item indicated by the specified seller SKU in the Small and Light program in the specified marketplace. If the item is not eligible, the ineligibility reasons are returned.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.SmallAndLightApi()
 = amazon_selling_partner_api.null() #  | The seller SKU that identifies the item.
 = amazon_selling_partner_api.null() #  | The marketplace in which to enroll the item. Note: Accepts a single marketplace only.

try:
    api_instance.put_small_and_light_enrollment_by_seller_sku(, )
except ApiException as e:
    print("Exception when calling SmallAndLightApi->put_small_and_light_enrollment_by_seller_sku: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The seller SKU that identifies the item. | 
 **** | [****](.md)| The marketplace in which to enroll the item. Note: Accepts a single marketplace only. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

