# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.fees_api import FeesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFeesApi(unittest.TestCase):
    """FeesApi unit test stubs"""

    def setUp(self):
        self.api = api.fees_api.FeesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_my_fees_estimate_for_asin(self):
        """Test case for get_my_fees_estimate_for_asin

        """
        pass

    def test_get_my_fees_estimate_for_sku(self):
        """Test case for get_my_fees_estimate_for_sku

        """
        pass


if __name__ == '__main__':
    unittest.main()