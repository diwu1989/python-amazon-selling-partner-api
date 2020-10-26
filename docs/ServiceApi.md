# amazon_selling_partner_api.ServiceApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_appointment_for_service_job_by_service_job_id**](ServiceApi.md#add_appointment_for_service_job_by_service_job_id) | **POST** /service/v1/serviceJobs/{serviceJobId}/appointments | 
[**cancel_service_job_by_service_job_id**](ServiceApi.md#cancel_service_job_by_service_job_id) | **PUT** /service/v1/serviceJobs/{serviceJobId}/cancellations | 
[**complete_service_job_by_service_job_id**](ServiceApi.md#complete_service_job_by_service_job_id) | **PUT** /service/v1/serviceJobs/{serviceJobId}/completions | 
[**get_service_job_by_service_job_id**](ServiceApi.md#get_service_job_by_service_job_id) | **GET** /service/v1/serviceJobs/{serviceJobId} | 
[**get_service_jobs**](ServiceApi.md#get_service_jobs) | **GET** /service/v1/serviceJobs | 
[**reschedule_appointment_for_service_job_by_service_job_id**](ServiceApi.md#reschedule_appointment_for_service_job_by_service_job_id) | **POST** /service/v1/serviceJobs/{serviceJobId}/appointments/{appointmentId} | 

# **add_appointment_for_service_job_by_service_job_id**
> add_appointment_for_service_job_by_service_job_id()



Adds an appointment to the service job indicated by the service job identifier you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 20 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ServiceApi()
 = amazon_selling_partner_api.null() #  | An Amazon defined service job identifier.

try:
    api_instance.add_appointment_for_service_job_by_service_job_id()
except ApiException as e:
    print("Exception when calling ServiceApi->add_appointment_for_service_job_by_service_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon defined service job identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_service_job_by_service_job_id**
> cancel_service_job_by_service_job_id(, )



Cancels the service job indicated by the service job identifier you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 20 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ServiceApi()
 = amazon_selling_partner_api.null() #  | An Amazon defined service job identifier.
 = amazon_selling_partner_api.null() #  | A cancel reason code that specifies the reason for cancelling a service job.

try:
    api_instance.cancel_service_job_by_service_job_id(, )
except ApiException as e:
    print("Exception when calling ServiceApi->cancel_service_job_by_service_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon defined service job identifier. | 
 **** | [****](.md)| A cancel reason code that specifies the reason for cancelling a service job. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_service_job_by_service_job_id**
> complete_service_job_by_service_job_id()



Completes the service job indicated by the service job identifier you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 20 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ServiceApi()
 = amazon_selling_partner_api.null() #  | An Amazon defined service job identifier.

try:
    api_instance.complete_service_job_by_service_job_id()
except ApiException as e:
    print("Exception when calling ServiceApi->complete_service_job_by_service_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon defined service job identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_job_by_service_job_id**
> get_service_job_by_service_job_id()



Gets service job details for the service job indicated by the service job identifier you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 20 | 40 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ServiceApi()
 = amazon_selling_partner_api.null() #  | A service job identifier.

try:
    api_instance.get_service_job_by_service_job_id()
except ApiException as e:
    print("Exception when calling ServiceApi->get_service_job_by_service_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| A service job identifier. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_jobs**
> get_service_jobs(, =, =, =, =, =, =, =, =, =, =, =, =)



Gets service job details for the specified filter query.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 10 | 40 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ServiceApi()
 = amazon_selling_partner_api.null() #  | Used to select jobs that were placed in the specified marketplaces. 
 = amazon_selling_partner_api.null() #  | List of service order ids for the query you want to perform.Max values supported 20.  (optional)
 = amazon_selling_partner_api.null() #  | A list of one or more job status by which to filter the list of jobs. (optional)
 = amazon_selling_partner_api.null() #  | String returned in the response of your previous request. (optional)
 = amazon_selling_partner_api.null() #  | A non-negative integer that indicates the maximum number of jobs to return in the list, Value must be 1 - 20. Default 20.  (optional)
 = amazon_selling_partner_api.null() #  | Sort fields on which you want to sort the output. (optional)
 = amazon_selling_partner_api.null() #  | Sort order for the query you want to perform. (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting jobs created after (or at) a specified time must be in ISO 8601 format. Required if LastUpdatedAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.  (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting jobs created before (or at) a specified time must be in ISO 8601 format.  (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting jobs updated after (or at) a specified time must be in ISO 8601 format. Required if createdAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.  (optional)
 = amazon_selling_partner_api.null() #  | A date used for selecting jobs updated before (or at) a specified time must be in ISO 8601 format.  (optional)
 = amazon_selling_partner_api.null() #  | A date used for filtering jobs schedule after (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.  (optional)
 = amazon_selling_partner_api.null() #  | A date used for filtering jobs schedule before (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.  (optional)

try:
    api_instance.get_service_jobs(, =, =, =, =, =, =, =, =, =, =, =, =)
except ApiException as e:
    print("Exception when calling ServiceApi->get_service_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| Used to select jobs that were placed in the specified marketplaces.  | 
 **** | [****](.md)| List of service order ids for the query you want to perform.Max values supported 20.  | [optional] 
 **** | [****](.md)| A list of one or more job status by which to filter the list of jobs. | [optional] 
 **** | [****](.md)| String returned in the response of your previous request. | [optional] 
 **** | [****](.md)| A non-negative integer that indicates the maximum number of jobs to return in the list, Value must be 1 - 20. Default 20.  | [optional] 
 **** | [****](.md)| Sort fields on which you want to sort the output. | [optional] 
 **** | [****](.md)| Sort order for the query you want to perform. | [optional] 
 **** | [****](.md)| A date used for selecting jobs created after (or at) a specified time must be in ISO 8601 format. Required if LastUpdatedAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.  | [optional] 
 **** | [****](.md)| A date used for selecting jobs created before (or at) a specified time must be in ISO 8601 format.  | [optional] 
 **** | [****](.md)| A date used for selecting jobs updated after (or at) a specified time must be in ISO 8601 format. Required if createdAfter is not specified.Specifying both CreatedAfter and LastUpdatedAfter returns an error.  | [optional] 
 **** | [****](.md)| A date used for selecting jobs updated before (or at) a specified time must be in ISO 8601 format.  | [optional] 
 **** | [****](.md)| A date used for filtering jobs schedule after (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.  | [optional] 
 **** | [****](.md)| A date used for filtering jobs schedule before (or at) a specified time must be in ISO 8601 format. schedule end date should not be earlier than schedule start date.  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reschedule_appointment_for_service_job_by_service_job_id**
> reschedule_appointment_for_service_job_by_service_job_id(, )



Reschedules an appointment for the service job indicated by the service job identifier you specify.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | 5 | 20 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.

### Example
```python
from __future__ import print_function
import time
import amazon_selling_partner_api
from amazon_selling_partner_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = amazon_selling_partner_api.ServiceApi()
 = amazon_selling_partner_api.null() #  | An Amazon defined service job identifier.
 = amazon_selling_partner_api.null() #  | An existing appointment identifier for the Service Job.

try:
    api_instance.reschedule_appointment_for_service_job_by_service_job_id(, )
except ApiException as e:
    print("Exception when calling ServiceApi->reschedule_appointment_for_service_job_by_service_job_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **** | [****](.md)| An Amazon defined service job identifier. | 
 **** | [****](.md)| An existing appointment identifier for the Service Job. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

