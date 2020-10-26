# amazon_selling_partner_api.FbaInboundApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_preorder**](FbaInboundApi.md#confirm_preorder) | **PUT** /fba/inbound/v0/shipments/{shipmentId}/preorder/confirm | 
[**confirm_transport**](FbaInboundApi.md#confirm_transport) | **POST** /fba/inbound/v0/shipments/{shipmentId}/transport/confirm | 
[**create_inbound_shipment**](FbaInboundApi.md#create_inbound_shipment) | **POST** /fba/inbound/v0/shipments/{shipmentId} | 
[**create_inbound_shipment_plan**](FbaInboundApi.md#create_inbound_shipment_plan) | **POST** /fba/inbound/v0/plans | 
[**estimate_transport**](FbaInboundApi.md#estimate_transport) | **POST** /fba/inbound/v0/shipments/{shipmentId}/transport/estimate | 
[**get_bill_of_lading**](FbaInboundApi.md#get_bill_of_lading) | **GET** /fba/inbound/v0/shipments/{shipmentId}/billOfLading | 
[**get_inbound_guidance**](FbaInboundApi.md#get_inbound_guidance) | **GET** /fba/inbound/v0/itemsGuidance | 
[**get_item_eligibility_preview**](FbaInboundApi.md#get_item_eligibility_preview) | **GET** /fba/inbound/v1/eligibility/itemPreview | 
[**get_labels**](FbaInboundApi.md#get_labels) | **GET** /fba/inbound/v0/shipments/{shipmentId}/labels | 
[**get_preorder_info**](FbaInboundApi.md#get_preorder_info) | **GET** /fba/inbound/v0/shipments/{shipmentId}/preorder | 
[**get_prep_instructions**](FbaInboundApi.md#get_prep_instructions) | **GET** /fba/inbound/v0/prepInstructions | 
[**get_shipment_items**](FbaInboundApi.md#get_shipment_items) | **GET** /fba/inbound/v0/shipmentItems | 
[**get_shipment_items_by_shipment_id**](FbaInboundApi.md#get_shipment_items_by_shipment_id) | **GET** /fba/inbound/v0/shipments/{shipmentId}/items | 
[**get_shipments**](FbaInboundApi.md#get_shipments) | **GET** /fba/inbound/v0/shipments | 
[**get_transport_details**](FbaInboundApi.md#get_transport_details) | **GET** /fba/inbound/v0/shipments/{shipmentId}/transport | 
[**put_transport_details**](FbaInboundApi.md#put_transport_details) | **PUT** /fba/inbound/v0/shipments/{shipmentId}/transport | 
[**update_inbound_shipment**](FbaInboundApi.md#update_inbound_shipment) | **PUT** /fba/inbound/v0/shipments/{shipmentId} | 
[**void_transport**](FbaInboundApi.md#void_transport) | **POST** /fba/inbound/v0/shipments/{shipmentId}/transport/void | 

# **confirm_preorder**
> confirm_preorder(, , )



Returns information needed to confirm a shipment for pre-order. Call this operation after calling the getPreorderInfo operation to get the NeedByDate value and other pre-order information about the shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.
 = amazon_selling_partner_api.null() #  | Date that the shipment must arrive at the Amazon fulfillment center to avoid delivery promise breaks for pre-ordered items. Must be in YYYY-MM-DD format. The response to the getPreorderInfo operation returns this value.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace the shipment is tied to.

try:
    api_instance.confirm_preorder(, , )
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_preorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 
 **** | [****](.md)| Date that the shipment must arrive at the Amazon fulfillment center to avoid delivery promise breaks for pre-ordered items. Must be in YYYY-MM-DD format. The response to the getPreorderInfo operation returns this value. | 
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace the shipment is tied to. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_transport**
> confirm_transport()



Confirms that the seller accepts the Amazon-partnered shipping estimate, agrees to allow Amazon to charge their account for the shipping cost, and requests that the Amazon-partnered carrier ship the inbound shipment.  Prior to calling the confirmTransport operation, you should call the getTransportDetails operation to get the Amazon-partnered shipping estimate.  Important: After confirming the transportation request, if the seller decides that they do not want the Amazon-partnered carrier to ship the inbound shipment, you can call the voidTransport operation to cancel the transportation request. Note that for a Small Parcel shipment, the seller has 24 hours after confirming a transportation request to void the transportation request. For a Less Than Truckload/Full Truckload (LTL/FTL) shipment, the seller has one hour after confirming a transportation request to void it. After the grace period has expired the seller's account will be charged for the shipping cost.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.confirm_transport()
except ApiException as e:
    print("Exception when calling FbaInboundApi->confirm_transport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbound_shipment**
> create_inbound_shipment()



Returns a new inbound shipment based on the specified shipmentId that was returned by the createInboundShipmentPlan operation.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.create_inbound_shipment()
except ApiException as e:
    print("Exception when calling FbaInboundApi->create_inbound_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_inbound_shipment_plan**
> create_inbound_shipment_plan()



Returns one or more inbound shipment plans, which provide the information you need to create one or more inbound shipments for a set of items that you specify. Multiple inbound shipment plans might be required so that items can be optimally placed in Amazon's fulfillment network—for example, positioning inventory closer to the customer. Alternatively, two inbound shipment plans might be created with the same Amazon fulfillment center destination if the two shipment plans require different processing—for example, items that require labels must be shipped separately from stickerless, commingled inventory.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()

try:
    api_instance.create_inbound_shipment_plan()
except ApiException as e:
    print("Exception when calling FbaInboundApi->create_inbound_shipment_plan: %s\n" % e)
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

# **estimate_transport**
> estimate_transport()



Initiates the process of estimating the shipping cost for an inbound shipment by an Amazon-partnered carrier.  Prior to calling the estimateTransport operation, you must call the putTransportDetails operation to provide Amazon with the transportation information for the inbound shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.estimate_transport()
except ApiException as e:
    print("Exception when calling FbaInboundApi->estimate_transport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bill_of_lading**
> get_bill_of_lading()



Returns a bill of lading for a Less Than Truckload/Full Truckload (LTL/FTL) shipment. The getBillOfLading operation returns PDF document data for printing a bill of lading for an Amazon-partnered Less Than Truckload/Full Truckload (LTL/FTL) inbound shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.get_bill_of_lading()
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_bill_of_lading: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_guidance**
> get_inbound_guidance(, =, =)



Returns information that lets a seller know if Amazon recommends sending an item to a given marketplace. In some cases, Amazon provides guidance for why a given SellerSKU or ASIN is not recommended for shipment to Amazon's fulfillment network. Sellers may still ship items that are not recommended, at their discretion.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace where the product would be stored.
 = amazon_selling_partner_api.null() #  | A list of SellerSKU values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: SellerSKU is qualified by the SellerId, which is included with every Selling Partner API operation that you submit. If you specify a SellerSKU that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.  (optional)
 = amazon_selling_partner_api.null() #  | A list of ASIN values. Used to identify items for which you want inbound guidance for shipment to Amazon's fulfillment network. Note: If you specify a ASIN that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold. (optional)

try:
    api_instance.get_inbound_guidance(, =, =)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_inbound_guidance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace where the product would be stored. | 
 **** | [****](.md)| A list of SellerSKU values. Used to identify items for which you want inbound guidance for shipment to Amazon&#x27;s fulfillment network. Note: SellerSKU is qualified by the SellerId, which is included with every Selling Partner API operation that you submit. If you specify a SellerSKU that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold.  | [optional] 
 **** | [****](.md)| A list of ASIN values. Used to identify items for which you want inbound guidance for shipment to Amazon&#x27;s fulfillment network. Note: If you specify a ASIN that identifies a variation parent ASIN, this operation returns an error. A variation parent ASIN represents a generic product that cannot be sold. Variation child ASINs represent products that have specific characteristics (such as size and color) and can be sold. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_eligibility_preview**
> get_item_eligibility_preview(, , =)



This operation gets an eligibility preview for an item that you specify. You can specify the type of eligibility preview that you want (INBOUND or COMMINGLING). For INBOUND previews, you can specify the marketplace in which you want to determine the item's eligibility.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 1 | 1 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | The ASIN of the item for which you want an eligibility preview.
 = amazon_selling_partner_api.null() #  | The program that you want to check eligibility against.
 = amazon_selling_partner_api.null() #  | The identifier for the marketplace in which you want to determine eligibility. Required only when program=INBOUND. (optional)

try:
    api_instance.get_item_eligibility_preview(, , =)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_item_eligibility_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The ASIN of the item for which you want an eligibility preview. | 
 **** | [****](.md)| The program that you want to check eligibility against. | 
 **** | [****](.md)| The identifier for the marketplace in which you want to determine eligibility. Required only when program&#x3D;INBOUND. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_labels**
> get_labels(, , , =, =, =)



Returns package/pallet labels for faster and more accurate shipment processing at the Amazon fulfillment center.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.
 = amazon_selling_partner_api.null() #  | The page type to use to print the labels. Submitting a PageType value that is not supported in your marketplace returns an error.
 = amazon_selling_partner_api.null() #  | The type of labels requested. 
 = amazon_selling_partner_api.null() #  | The number of packages in the shipment. (optional)
 = amazon_selling_partner_api.null() #  | A list of identifiers that specify packages for which you want package labels printed.  Must match CartonId values previously passed using the FBA Inbound Shipment Carton Information Feed. If not, the operation returns the IncorrectPackageIdentifier error code. (optional)
 = amazon_selling_partner_api.null() #  | The number of pallets in the shipment. This returns four identical labels for each pallet. (optional)

try:
    api_instance.get_labels(, , , =, =, =)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 
 **** | [****](.md)| The page type to use to print the labels. Submitting a PageType value that is not supported in your marketplace returns an error. | 
 **** | [****](.md)| The type of labels requested.  | 
 **** | [****](.md)| The number of packages in the shipment. | [optional] 
 **** | [****](.md)| A list of identifiers that specify packages for which you want package labels printed.  Must match CartonId values previously passed using the FBA Inbound Shipment Carton Information Feed. If not, the operation returns the IncorrectPackageIdentifier error code. | [optional] 
 **** | [****](.md)| The number of pallets in the shipment. This returns four identical labels for each pallet. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preorder_info**
> get_preorder_info(, )



Returns pre-order information, including dates, that a seller needs before confirming a shipment for pre-order.   **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace the shipment is tied to.

try:
    api_instance.get_preorder_info(, )
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_preorder_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace the shipment is tied to. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prep_instructions**
> get_prep_instructions(, =, =)



Returns labeling requirements and item preparation instructions to help prepare items for shipment to Amazon's fulfillment network.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | The country code of the country to which the items will be shipped. Note that labeling requirements and item preparation instructions can vary by country.
 = amazon_selling_partner_api.null() #  | A list of SellerSKU values. Used to identify items for which you want labeling requirements and item preparation instructions for shipment to Amazon's fulfillment network. The SellerSKU is qualified by the Seller ID, which is included with every call to the Seller Partner API.  Note: Include seller SKUs that you have used to list items on Amazon's retail website. If you include a seller SKU that you have never used to list an item on Amazon's retail website, the seller SKU is returned in the InvalidSKUList property in the response. (optional)
 = amazon_selling_partner_api.null() #  | A list of ASIN values. Used to identify items for which you want item preparation instructions to help with item sourcing decisions.  Note: ASINs must be included in the product catalog for at least one of the marketplaces that the seller  participates in. Any ASIN that is not included in the product catalog for at least one of the marketplaces that the seller participates in is returned in the InvalidASINList property in the response. You can find out which marketplaces a seller participates in by calling the getMarketplaceParticipations operation in the Selling Partner API for Sellers. (optional)

try:
    api_instance.get_prep_instructions(, =, =)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_prep_instructions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| The country code of the country to which the items will be shipped. Note that labeling requirements and item preparation instructions can vary by country. | 
 **** | [****](.md)| A list of SellerSKU values. Used to identify items for which you want labeling requirements and item preparation instructions for shipment to Amazon&#x27;s fulfillment network. The SellerSKU is qualified by the Seller ID, which is included with every call to the Seller Partner API.  Note: Include seller SKUs that you have used to list items on Amazon&#x27;s retail website. If you include a seller SKU that you have never used to list an item on Amazon&#x27;s retail website, the seller SKU is returned in the InvalidSKUList property in the response. | [optional] 
 **** | [****](.md)| A list of ASIN values. Used to identify items for which you want item preparation instructions to help with item sourcing decisions.  Note: ASINs must be included in the product catalog for at least one of the marketplaces that the seller  participates in. Any ASIN that is not included in the product catalog for at least one of the marketplaces that the seller participates in is returned in the InvalidASINList property in the response. You can find out which marketplaces a seller participates in by calling the getMarketplaceParticipations operation in the Selling Partner API for Sellers. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_items**
> get_shipment_items(, , =, =, =)



Returns a list of items in a specified inbound shipment, or a list of items that were updated within a specified time frame.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | Indicates whether items are returned using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or using NextToken, which continues returning items specified in a previous request.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace where the product would be stored.
 = amazon_selling_partner_api.null() #  | A date used for selecting inbound shipment items that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting inbound shipment items that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response to your previous request. (optional)

try:
    api_instance.get_shipment_items(, , =, =, =)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_shipment_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| Indicates whether items are returned using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or using NextToken, which continues returning items specified in a previous request. | 
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace where the product would be stored. | 
 **** | [****](.md)| A date used for selecting inbound shipment items that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller. | [optional] 
 **** | [****](.md)| A date used for selecting inbound shipment items that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller. | [optional] 
 **** | [****](.md)| A string token returned in the response to your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_items_by_shipment_id**
> get_shipment_items_by_shipment_id(, )



Returns a list of items in a specified inbound shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier used for selecting items in a specific inbound shipment.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace where the product would be stored.

try:
    api_instance.get_shipment_items_by_shipment_id(, )
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_shipment_items_by_shipment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier used for selecting items in a specific inbound shipment. | 
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace where the product would be stored. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipments**
> get_shipments(, , =, =, =, =, =)



Returns a list of inbound shipments based on criteria that you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | Indicates whether shipments are returned using shipment information (by providing the ShipmentStatusList or ShipmentIdList parameters), using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or by using NextToken to continue returning items specified in a previous request.
 = amazon_selling_partner_api.null() #  | A marketplace identifier. Specifies the marketplace where the product would be stored.
 = amazon_selling_partner_api.null() #  | A list of ShipmentStatus values. Used to select shipments with a current status that matches the status values that you specify. (optional)
 = amazon_selling_partner_api.null() #  | A list of shipment IDs used to select the shipments that you want. If both ShipmentStatusList and ShipmentIdList are specified, only shipments that match both parameters are returned. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting inbound shipments that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting inbound shipments that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller. (optional)
 = amazon_selling_partner_api.null() #  | A string token returned in the response to your previous request. (optional)

try:
    api_instance.get_shipments(, , =, =, =, =, =)
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_shipments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| Indicates whether shipments are returned using shipment information (by providing the ShipmentStatusList or ShipmentIdList parameters), using a date range (by providing the LastUpdatedAfter and LastUpdatedBefore parameters), or by using NextToken to continue returning items specified in a previous request. | 
 **** | [****](.md)| A marketplace identifier. Specifies the marketplace where the product would be stored. | 
 **** | [****](.md)| A list of ShipmentStatus values. Used to select shipments with a current status that matches the status values that you specify. | [optional] 
 **** | [****](.md)| A list of shipment IDs used to select the shipments that you want. If both ShipmentStatusList and ShipmentIdList are specified, only shipments that match both parameters are returned. | [optional] 
 **** | [****](.md)| A date used for selecting inbound shipments that were last updated after (or at) a specified time. The selection includes updates made by Amazon and by the seller. | [optional] 
 **** | [****](.md)| A date used for selecting inbound shipments that were last updated before (or at) a specified time. The selection includes updates made by Amazon and by the seller. | [optional] 
 **** | [****](.md)| A string token returned in the response to your previous request. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transport_details**
> get_transport_details()



Returns current transportation information about an inbound shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.get_transport_details()
except ApiException as e:
    print("Exception when calling FbaInboundApi->get_transport_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_transport_details**
> put_transport_details()



Sends transportation information to Amazon about an inbound shipment.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.put_transport_details()
except ApiException as e:
    print("Exception when calling FbaInboundApi->put_transport_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_shipment**
> update_inbound_shipment()



Adds, updates, or removes items from the inbound shipment identified by the specified shipment identifier.   **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.update_inbound_shipment()
except ApiException as e:
    print("Exception when calling FbaInboundApi->update_inbound_shipment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **void_transport**
> void_transport()



Cancels a previously-confirmed request to ship an inbound shipment using an Amazon-partnered carrier.  To be successful, you must call this operation before the VoidDeadline date that is returned by the getTransportDetails operation.  Important: The VoidDeadline date is 24 hours after you confirm a Small Parcel shipment transportation request or one hour after you confirm a Less Than Truckload/Full Truckload (LTL/FTL) shipment transportation request. After the void deadline passes, your account will be charged for the shipping cost.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 2 | 30 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.FbaInboundApi()
 = amazon_selling_partner_api.null() #  | A shipment identifier originally returned by the createInboundShipmentPlan operation.

try:
    api_instance.void_transport()
except ApiException as e:
    print("Exception when calling FbaInboundApi->void_transport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A shipment identifier originally returned by the createInboundShipmentPlan operation. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

