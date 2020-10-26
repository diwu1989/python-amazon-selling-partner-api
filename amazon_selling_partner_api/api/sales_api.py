# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from amazon_selling_partner_api.api_client import ApiClient


class SalesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_order_metrics(self, , , , **kwargs):  # noqa: E501
        """get_order_metrics  # noqa: E501

        Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | .5 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_metrics(, , , async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : A list of marketplace identifiers. Example: ATVPDKIKX0DER indicates the US marketplace. (required)
        :param  : A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone. (required)
        :param  : The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone. (required)
        :param  : An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone.
        :param  : Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers.
        :param  : Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (Amazon fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network.
        :param  : Specifies the day that the week starts on when granularity=Week, either Monday or Sunday. Default: Monday. Example: Sunday, if you want the week to start on a Sunday.
        :param  : Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
        :param  : Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_order_metrics_with_http_info(, , , **kwargs)  # noqa: E501
        else:
            (data) = self.get_order_metrics_with_http_info(, , , **kwargs)  # noqa: E501
            return data

    def get_order_metrics_with_http_info(self, , , , **kwargs):  # noqa: E501
        """get_order_metrics  # noqa: E501

        Returns aggregated order metrics for given interval, broken down by granularity, for given buyer type.  **Usage Plan:**  | Rate (requests per second) | Burst | | ---- | ---- | | .5 | 15 |  For more information, see \"Usage Plans and Rate Limits\" in the Selling Partner API documentation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_order_metrics_with_http_info(, , , async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param  : A list of marketplace identifiers. Example: ATVPDKIKX0DER indicates the US marketplace. (required)
        :param  : A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone. (required)
        :param  : The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone. (required)
        :param  : An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone.
        :param  : Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers.
        :param  : Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (Amazon fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only Amazon fulfillment network.
        :param  : Specifies the day that the week starts on when granularity=Week, either Monday or Sunday. Default: Monday. Example: Sunday, if you want the week to start on a Sunday.
        :param  : Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
        :param  : Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['', '', '', '', '', '', '', '', '']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_metrics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '' is set
        if ('' not in params or
                params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `get_order_metrics`")  # noqa: E501
        # verify the required parameter '' is set
        if ('' not in params or
                params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `get_order_metrics`")  # noqa: E501
        # verify the required parameter '' is set
        if ('' not in params or
                params[''] is None):
            raise ValueError("Missing the required parameter `` when calling `get_order_metrics`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if '' in params:
            query_params.append(('marketplaceIds', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('interval', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('granularityTimeZone', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('granularity', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('buyerType', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('fulfillmentNetwork', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('firstDayOfWeek', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('asin', params['']))  # noqa: E501
        if '' in params:
            query_params.append(('sku', params['']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sales/v1/orderMetrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)