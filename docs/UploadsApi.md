# amazon_selling_partner_api.UploadsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_upload_destination_for_resource**](UploadsApi.md#create_upload_destination_for_resource) | **POST** /uploads/2020-11-01/uploadDestinations/{resource} | 

# **create_upload_destination_for_resource**
> create_upload_destination_for_resource(, , , =)



Creates an upload destination for a resource that you specify and returns the information required to upload to that destination.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | .1 | 5 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.UploadsApi()
 = amazon_selling_partner_api.null() #  | A list of marketplace identifiers. This specifies the marketplaces where the upload will be available. Only one marketplace can be specified.
 = amazon_selling_partner_api.null() #  | An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit.
 = amazon_selling_partner_api.null() #  | The URL of the resource for the upload destination that you are creating. For example, to create an upload destination for a Buyer-Seller Messaging message, the {resource} would be /messaging and the path would be  /uploads/v1/uploadDestinations/messaging
 = amazon_selling_partner_api.null() #  | The content type of the file to be uploaded. (optional)

try:
    api_instance.create_upload_destination_for_resource(, , , =)
except ApiException as e:
    print("Exception when calling UploadsApi->create_upload_destination_for_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A list of marketplace identifiers. This specifies the marketplaces where the upload will be available. Only one marketplace can be specified. | 
 **** | [****](.md)| An MD5 hash of the content to be submitted to the upload destination. This value is used to determine if the data has been corrupted or tampered with during transit. | 
 **** | [****](.md)| The URL of the resource for the upload destination that you are creating. For example, to create an upload destination for a Buyer-Seller Messaging message, the {resource} would be /messaging and the path would be  /uploads/v1/uploadDestinations/messaging | 
 **** | [****](.md)| The content type of the file to be uploaded. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

