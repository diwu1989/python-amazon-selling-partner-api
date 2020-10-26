# swagger-client
The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://sellercentral.amazon.com/gp/mws/contactus.html](https://sellercentral.amazon.com/gp/mws/contactus.html)

Created using nodejs tool `openapi-merge-cli`.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthorizationApi(swagger_client.ApiClient(configuration))
 = swagger_client.null() #  | The seller ID of the seller for whom you are requesting Selling Partner API authorization. This must be the seller ID of the seller who authorized your application on the Marketplace Appstore.
 = swagger_client.null() #  | Your developer ID. This must be one of the developer ID values that you provided when you registered your application in Developer Central.
 = swagger_client.null() #  | The MWS Auth Token that was generated when the seller authorized your application on the Marketplace Appstore.

try:
    # Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.
    api_instance.get_authorization_code(, , )
except ApiException as e:
    print("Exception when calling AuthorizationApi->get_authorization_code: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to */*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthorizationApi* | [**get_authorization_code**](docs/AuthorizationApi.md#get_authorization_code) | **GET** /authorization/v1/authorizationCode | Returns the Login with Amazon (LWA) authorization code for an existing Amazon MWS authorization.
*CatalogApi* | [**get_catalog_item**](docs/CatalogApi.md#get_catalog_item) | **GET** /catalog/v0/items/{asin} | 
*CatalogApi* | [**list_catalog_categories**](docs/CatalogApi.md#list_catalog_categories) | **GET** /catalog/v0/categories | 
*CatalogApi* | [**list_catalog_items**](docs/CatalogApi.md#list_catalog_items) | **GET** /catalog/v0/items | 
*DefaultApi* | [**list_financial_event_groups**](docs/DefaultApi.md#list_financial_event_groups) | **GET** /finances/v0/financialEventGroups | 
*DefaultApi* | [**list_financial_events**](docs/DefaultApi.md#list_financial_events) | **GET** /finances/v0/financialEvents | 
*DefaultApi* | [**list_financial_events_by_group_id**](docs/DefaultApi.md#list_financial_events_by_group_id) | **GET** /finances/v0/financialEventGroups/{eventGroupId}/financialEvents | 
*DefaultApi* | [**list_financial_events_by_order_id**](docs/DefaultApi.md#list_financial_events_by_order_id) | **GET** /finances/v0/orders/{orderId}/financialEvents | 
*FbaInboundApi* | [**confirm_preorder**](docs/FbaInboundApi.md#confirm_preorder) | **PUT** /fba/inbound/v0/shipments/{shipmentId}/preorder/confirm | 
*FbaInboundApi* | [**confirm_transport**](docs/FbaInboundApi.md#confirm_transport) | **POST** /fba/inbound/v0/shipments/{shipmentId}/transport/confirm | 
*FbaInboundApi* | [**create_inbound_shipment**](docs/FbaInboundApi.md#create_inbound_shipment) | **POST** /fba/inbound/v0/shipments/{shipmentId} | 
*FbaInboundApi* | [**create_inbound_shipment_plan**](docs/FbaInboundApi.md#create_inbound_shipment_plan) | **POST** /fba/inbound/v0/plans | 
*FbaInboundApi* | [**estimate_transport**](docs/FbaInboundApi.md#estimate_transport) | **POST** /fba/inbound/v0/shipments/{shipmentId}/transport/estimate | 
*FbaInboundApi* | [**get_bill_of_lading**](docs/FbaInboundApi.md#get_bill_of_lading) | **GET** /fba/inbound/v0/shipments/{shipmentId}/billOfLading | 
*FbaInboundApi* | [**get_inbound_guidance**](docs/FbaInboundApi.md#get_inbound_guidance) | **GET** /fba/inbound/v0/itemsGuidance | 
*FbaInboundApi* | [**get_item_eligibility_preview**](docs/FbaInboundApi.md#get_item_eligibility_preview) | **GET** /fba/inbound/v1/eligibility/itemPreview | 
*FbaInboundApi* | [**get_labels**](docs/FbaInboundApi.md#get_labels) | **GET** /fba/inbound/v0/shipments/{shipmentId}/labels | 
*FbaInboundApi* | [**get_preorder_info**](docs/FbaInboundApi.md#get_preorder_info) | **GET** /fba/inbound/v0/shipments/{shipmentId}/preorder | 
*FbaInboundApi* | [**get_prep_instructions**](docs/FbaInboundApi.md#get_prep_instructions) | **GET** /fba/inbound/v0/prepInstructions | 
*FbaInboundApi* | [**get_shipment_items**](docs/FbaInboundApi.md#get_shipment_items) | **GET** /fba/inbound/v0/shipmentItems | 
*FbaInboundApi* | [**get_shipment_items_by_shipment_id**](docs/FbaInboundApi.md#get_shipment_items_by_shipment_id) | **GET** /fba/inbound/v0/shipments/{shipmentId}/items | 
*FbaInboundApi* | [**get_shipments**](docs/FbaInboundApi.md#get_shipments) | **GET** /fba/inbound/v0/shipments | 
*FbaInboundApi* | [**get_transport_details**](docs/FbaInboundApi.md#get_transport_details) | **GET** /fba/inbound/v0/shipments/{shipmentId}/transport | 
*FbaInboundApi* | [**put_transport_details**](docs/FbaInboundApi.md#put_transport_details) | **PUT** /fba/inbound/v0/shipments/{shipmentId}/transport | 
*FbaInboundApi* | [**update_inbound_shipment**](docs/FbaInboundApi.md#update_inbound_shipment) | **PUT** /fba/inbound/v0/shipments/{shipmentId} | 
*FbaInboundApi* | [**void_transport**](docs/FbaInboundApi.md#void_transport) | **POST** /fba/inbound/v0/shipments/{shipmentId}/transport/void | 
*FbaInventoryApi* | [**get_inventory_summaries**](docs/FbaInventoryApi.md#get_inventory_summaries) | **GET** /fba/inventory/v1/summaries | 
*FbaOutboundApi* | [**cancel_fulfillment_order**](docs/FbaOutboundApi.md#cancel_fulfillment_order) | **PUT** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel | 
*FbaOutboundApi* | [**create_fulfillment_order**](docs/FbaOutboundApi.md#create_fulfillment_order) | **POST** /fba/outbound/v0/fulfillmentOrders | 
*FbaOutboundApi* | [**create_fulfillment_return**](docs/FbaOutboundApi.md#create_fulfillment_return) | **PUT** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId}/return | 
*FbaOutboundApi* | [**get_fulfillment_order**](docs/FbaOutboundApi.md#get_fulfillment_order) | **GET** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId} | 
*FbaOutboundApi* | [**get_fulfillment_preview**](docs/FbaOutboundApi.md#get_fulfillment_preview) | **POST** /fba/outbound/v0/fulfillmentOrders/preview | 
*FbaOutboundApi* | [**get_package_tracking_details**](docs/FbaOutboundApi.md#get_package_tracking_details) | **GET** /fba/outbound/v0/tracking | 
*FbaOutboundApi* | [**list_all_fulfillment_orders**](docs/FbaOutboundApi.md#list_all_fulfillment_orders) | **GET** /fba/outbound/v0/fulfillmentOrders | 
*FbaOutboundApi* | [**list_return_reason_codes**](docs/FbaOutboundApi.md#list_return_reason_codes) | **GET** /fba/outbound/v0/returnReasonCodes | 
*FbaOutboundApi* | [**update_fulfillment_order**](docs/FbaOutboundApi.md#update_fulfillment_order) | **PUT** /fba/outbound/v0/fulfillmentOrders/{sellerFulfillmentOrderId} | 
*FeedsApi* | [**cancel_feed**](docs/FeedsApi.md#cancel_feed) | **DELETE** /feeds/2020-09-04/feeds/{feedId} | 
*FeedsApi* | [**create_feed**](docs/FeedsApi.md#create_feed) | **POST** /feeds/2020-09-04/feeds | 
*FeedsApi* | [**create_feed_document**](docs/FeedsApi.md#create_feed_document) | **POST** /feeds/2020-09-04/documents | 
*FeedsApi* | [**get_feed**](docs/FeedsApi.md#get_feed) | **GET** /feeds/2020-09-04/feeds/{feedId} | 
*FeedsApi* | [**get_feed_document**](docs/FeedsApi.md#get_feed_document) | **GET** /feeds/2020-09-04/documents/{feedDocumentId} | 
*FeedsApi* | [**get_feeds**](docs/FeedsApi.md#get_feeds) | **GET** /feeds/2020-09-04/feeds | 
*FeesApi* | [**get_my_fees_estimate_for_asin**](docs/FeesApi.md#get_my_fees_estimate_for_asin) | **POST** /products/fees/v0/items/{Asin}/feesEstimate | 
*FeesApi* | [**get_my_fees_estimate_for_sku**](docs/FeesApi.md#get_my_fees_estimate_for_sku) | **POST** /products/fees/v0/listings/{SellerSKU}/feesEstimate | 
*MerchantFulfillmentApi* | [**cancel_shipment**](docs/MerchantFulfillmentApi.md#cancel_shipment) | **DELETE** /mfn/v0/shipments/{shipmentId} | 
*MerchantFulfillmentApi* | [**cancel_shipment_old**](docs/MerchantFulfillmentApi.md#cancel_shipment_old) | **PUT** /mfn/v0/shipments/{shipmentId}/cancel | 
*MerchantFulfillmentApi* | [**create_shipment**](docs/MerchantFulfillmentApi.md#create_shipment) | **POST** /mfn/v0/shipments | 
*MerchantFulfillmentApi* | [**get_additional_seller_inputs**](docs/MerchantFulfillmentApi.md#get_additional_seller_inputs) | **POST** /mfn/v0/additionalSellerInputs | 
*MerchantFulfillmentApi* | [**get_additional_seller_inputs_old**](docs/MerchantFulfillmentApi.md#get_additional_seller_inputs_old) | **POST** /mfn/v0/sellerInputs | 
*MerchantFulfillmentApi* | [**get_eligible_shipment_services**](docs/MerchantFulfillmentApi.md#get_eligible_shipment_services) | **POST** /mfn/v0/eligibleShippingServices | 
*MerchantFulfillmentApi* | [**get_eligible_shipment_services_old**](docs/MerchantFulfillmentApi.md#get_eligible_shipment_services_old) | **POST** /mfn/v0/eligibleServices | 
*MerchantFulfillmentApi* | [**get_shipment**](docs/MerchantFulfillmentApi.md#get_shipment) | **GET** /mfn/v0/shipments/{shipmentId} | 
*MessagingApi* | [**confirm_customization_details**](docs/MessagingApi.md#confirm_customization_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmCustomizationDetails | 
*MessagingApi* | [**create_amazon_motors**](docs/MessagingApi.md#create_amazon_motors) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/amazonMotors | 
*MessagingApi* | [**create_confirm_delivery_details**](docs/MessagingApi.md#create_confirm_delivery_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmDeliveryDetails | 
*MessagingApi* | [**create_confirm_order_details**](docs/MessagingApi.md#create_confirm_order_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmOrderDetails | 
*MessagingApi* | [**create_confirm_service_details**](docs/MessagingApi.md#create_confirm_service_details) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/confirmServiceDetails | 
*MessagingApi* | [**create_digital_access_key**](docs/MessagingApi.md#create_digital_access_key) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/digitalAccessKey | 
*MessagingApi* | [**create_legal_disclosure**](docs/MessagingApi.md#create_legal_disclosure) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/legalDisclosure | 
*MessagingApi* | [**create_negative_feedback_removal**](docs/MessagingApi.md#create_negative_feedback_removal) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/negativeFeedbackRemoval | 
*MessagingApi* | [**create_unexpected_problem**](docs/MessagingApi.md#create_unexpected_problem) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/unexpectedProblem | 
*MessagingApi* | [**create_warranty**](docs/MessagingApi.md#create_warranty) | **POST** /messaging/v1/orders/{amazonOrderId}/messages/warranty | 
*MessagingApi* | [**get_attributes**](docs/MessagingApi.md#get_attributes) | **GET** /messaging/v1/orders/{amazonOrderId}/attributes | 
*MessagingApi* | [**get_messaging_actions_for_order**](docs/MessagingApi.md#get_messaging_actions_for_order) | **GET** /messaging/v1/orders/{amazonOrderId} | 
*NotificationsApi* | [**create_destination**](docs/NotificationsApi.md#create_destination) | **POST** /notifications/v1/destinations | 
*NotificationsApi* | [**create_subscription**](docs/NotificationsApi.md#create_subscription) | **POST** /notifications/v1/subscriptions/{notificationType} | 
*NotificationsApi* | [**delete_destination**](docs/NotificationsApi.md#delete_destination) | **DELETE** /notifications/v1/destinations/{destinationId} | 
*NotificationsApi* | [**delete_subscription_by_id**](docs/NotificationsApi.md#delete_subscription_by_id) | **DELETE** /notifications/v1/subscriptions/{notificationType}/{subscriptionId} | 
*NotificationsApi* | [**get_destination**](docs/NotificationsApi.md#get_destination) | **GET** /notifications/v1/destinations/{destinationId} | 
*NotificationsApi* | [**get_destinations**](docs/NotificationsApi.md#get_destinations) | **GET** /notifications/v1/destinations | 
*NotificationsApi* | [**get_subscription**](docs/NotificationsApi.md#get_subscription) | **GET** /notifications/v1/subscriptions/{notificationType} | 
*NotificationsApi* | [**get_subscription_by_id**](docs/NotificationsApi.md#get_subscription_by_id) | **GET** /notifications/v1/subscriptions/{notificationType}/{subscriptionId} | 
*OrdersV0Api* | [**get_order**](docs/OrdersV0Api.md#get_order) | **GET** /orders/v0/orders/{orderId} | 
*OrdersV0Api* | [**get_order_address**](docs/OrdersV0Api.md#get_order_address) | **GET** /orders/v0/orders/{orderId}/address | 
*OrdersV0Api* | [**get_order_buyer_info**](docs/OrdersV0Api.md#get_order_buyer_info) | **GET** /orders/v0/orders/{orderId}/buyerInfo | 
*OrdersV0Api* | [**get_order_items**](docs/OrdersV0Api.md#get_order_items) | **GET** /orders/v0/orders/{orderId}/orderItems | 
*OrdersV0Api* | [**get_order_items_buyer_info**](docs/OrdersV0Api.md#get_order_items_buyer_info) | **GET** /orders/v0/orders/{orderId}/orderItems/buyerInfo | 
*OrdersV0Api* | [**get_orders**](docs/OrdersV0Api.md#get_orders) | **GET** /orders/v0/orders | 
*ProductPricingApi* | [**get_competitive_pricing**](docs/ProductPricingApi.md#get_competitive_pricing) | **GET** /products/pricing/v0/competitivePrice | 
*ProductPricingApi* | [**get_item_offers**](docs/ProductPricingApi.md#get_item_offers) | **GET** /products/pricing/v0/items/{Asin}/offers | 
*ProductPricingApi* | [**get_listing_offers**](docs/ProductPricingApi.md#get_listing_offers) | **GET** /products/pricing/v0/listings/{SellerSKU}/offers | 
*ProductPricingApi* | [**get_pricing**](docs/ProductPricingApi.md#get_pricing) | **GET** /products/pricing/v0/price | 
*ReportsApi* | [**cancel_report**](docs/ReportsApi.md#cancel_report) | **DELETE** /reports/2020-09-04/reports/{reportId} | 
*ReportsApi* | [**cancel_report_schedule**](docs/ReportsApi.md#cancel_report_schedule) | **DELETE** /reports/2020-09-04/schedules/{reportScheduleId} | 
*ReportsApi* | [**create_report**](docs/ReportsApi.md#create_report) | **POST** /reports/2020-09-04/reports | 
*ReportsApi* | [**create_report_schedule**](docs/ReportsApi.md#create_report_schedule) | **POST** /reports/2020-09-04/schedules | 
*ReportsApi* | [**get_report**](docs/ReportsApi.md#get_report) | **GET** /reports/2020-09-04/reports/{reportId} | 
*ReportsApi* | [**get_report_document**](docs/ReportsApi.md#get_report_document) | **GET** /reports/2020-09-04/documents/{reportDocumentId} | 
*ReportsApi* | [**get_report_schedule**](docs/ReportsApi.md#get_report_schedule) | **GET** /reports/2020-09-04/schedules/{reportScheduleId} | 
*ReportsApi* | [**get_report_schedules**](docs/ReportsApi.md#get_report_schedules) | **GET** /reports/2020-09-04/schedules | 
*ReportsApi* | [**get_reports**](docs/ReportsApi.md#get_reports) | **GET** /reports/2020-09-04/reports | 
*SalesApi* | [**get_order_metrics**](docs/SalesApi.md#get_order_metrics) | **GET** /sales/v1/orderMetrics | 
*SellersApi* | [**get_marketplace_participations**](docs/SellersApi.md#get_marketplace_participations) | **GET** /sellers/v1/marketplaceParticipations | 
*ServiceApi* | [**add_appointment_for_service_job_by_service_job_id**](docs/ServiceApi.md#add_appointment_for_service_job_by_service_job_id) | **POST** /service/v1/serviceJobs/{serviceJobId}/appointments | 
*ServiceApi* | [**cancel_service_job_by_service_job_id**](docs/ServiceApi.md#cancel_service_job_by_service_job_id) | **PUT** /service/v1/serviceJobs/{serviceJobId}/cancellations | 
*ServiceApi* | [**complete_service_job_by_service_job_id**](docs/ServiceApi.md#complete_service_job_by_service_job_id) | **PUT** /service/v1/serviceJobs/{serviceJobId}/completions | 
*ServiceApi* | [**get_service_job_by_service_job_id**](docs/ServiceApi.md#get_service_job_by_service_job_id) | **GET** /service/v1/serviceJobs/{serviceJobId} | 
*ServiceApi* | [**get_service_jobs**](docs/ServiceApi.md#get_service_jobs) | **GET** /service/v1/serviceJobs | 
*ServiceApi* | [**reschedule_appointment_for_service_job_by_service_job_id**](docs/ServiceApi.md#reschedule_appointment_for_service_job_by_service_job_id) | **POST** /service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId} | 
*ShippingApi* | [**cancel_shipment**](docs/ShippingApi.md#cancel_shipment) | **POST** /shipping/v1/shipments/{shipmentId}/cancel | 
*ShippingApi* | [**create_shipment**](docs/ShippingApi.md#create_shipment) | **POST** /shipping/v1/shipments | 
*ShippingApi* | [**get_account**](docs/ShippingApi.md#get_account) | **GET** /shipping/v1/account | 
*ShippingApi* | [**get_rates**](docs/ShippingApi.md#get_rates) | **POST** /shipping/v1/rates | 
*ShippingApi* | [**get_shipment**](docs/ShippingApi.md#get_shipment) | **GET** /shipping/v1/shipments/{shipmentId} | 
*ShippingApi* | [**get_tracking_information**](docs/ShippingApi.md#get_tracking_information) | **GET** /shipping/v1/tracking/{trackingId} | 
*ShippingApi* | [**purchase_labels**](docs/ShippingApi.md#purchase_labels) | **POST** /shipping/v1/shipments/{shipmentId}/purchaseLabels | 
*ShippingApi* | [**purchase_shipment**](docs/ShippingApi.md#purchase_shipment) | **POST** /shipping/v1/purchaseShipment | 
*ShippingApi* | [**retrieve_shipping_label**](docs/ShippingApi.md#retrieve_shipping_label) | **POST** /shipping/v1/shipments/{shipmentId}/containers/{trackingId}/label | 
*SmallAndLightApi* | [**delete_small_and_light_enrollment_by_seller_sku**](docs/SmallAndLightApi.md#delete_small_and_light_enrollment_by_seller_sku) | **DELETE** /fba/smallAndLight/v1/enrollments/{sellerSKU} | 
*SmallAndLightApi* | [**get_small_and_light_eligibility_by_seller_sku**](docs/SmallAndLightApi.md#get_small_and_light_eligibility_by_seller_sku) | **GET** /fba/smallAndLight/v1/eligibilities/{sellerSKU} | 
*SmallAndLightApi* | [**get_small_and_light_enrollment_by_seller_sku**](docs/SmallAndLightApi.md#get_small_and_light_enrollment_by_seller_sku) | **GET** /fba/smallAndLight/v1/enrollments/{sellerSKU} | 
*SmallAndLightApi* | [**get_small_and_light_fee_preview**](docs/SmallAndLightApi.md#get_small_and_light_fee_preview) | **POST** /fba/smallAndLight/v1/feePreviews | 
*SmallAndLightApi* | [**put_small_and_light_enrollment_by_seller_sku**](docs/SmallAndLightApi.md#put_small_and_light_enrollment_by_seller_sku) | **PUT** /fba/smallAndLight/v1/enrollments/{sellerSKU} | 
*SolicitationsApi* | [**create_product_review_and_seller_feedback_solicitation**](docs/SolicitationsApi.md#create_product_review_and_seller_feedback_solicitation) | **POST** /solicitations/v1/orders/{amazonOrderId}/solicitations/productReviewAndSellerFeedback | 
*SolicitationsApi* | [**get_solicitation_actions_for_order**](docs/SolicitationsApi.md#get_solicitation_actions_for_order) | **GET** /solicitations/v1/orders/{amazonOrderId} | 
*UploadsApi* | [**create_upload_destination_for_resource**](docs/UploadsApi.md#create_upload_destination_for_resource) | **POST** /uploads/2020-11-01/uploadDestinations/{resource} | 

## Documentation For Models


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

