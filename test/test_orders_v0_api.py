# coding: utf-8

"""
    Selling Partner API for Catalog Items

    The Selling Partner API for Catalog Items helps you programmatically retrieve item details for items in the catalog.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import amazon_selling_partner_api
from amazon_selling_partner_api.api.orders_v0_api import OrdersV0Api  # noqa: E501
from amazon_selling_partner_api.rest import ApiException


class TestOrdersV0Api(unittest.TestCase):
    """OrdersV0Api unit test stubs"""

    def setUp(self):
        self.api = OrdersV0Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_order(self):
        """Test case for get_order

        """
        pass

    def test_get_order_address(self):
        """Test case for get_order_address

        """
        pass

    def test_get_order_buyer_info(self):
        """Test case for get_order_buyer_info

        """
        pass

    def test_get_order_items(self):
        """Test case for get_order_items

        """
        pass

    def test_get_order_items_buyer_info(self):
        """Test case for get_order_items_buyer_info

        """
        pass

    def test_get_orders(self):
        """Test case for get_orders

        """
        pass


if __name__ == '__main__':
    unittest.main()
