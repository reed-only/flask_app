"""
Tests for bananas resource
"""

from unittest import TestCase

import requests

from tests.resources import API_HOST


class TestBananas(TestCase):
    """
    Tests for bananas resource
    """
    def test_get_bananas(self):
        """
        Test get bananas
        """
        response = requests.get(API_HOST + '/bananas')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_get_banana(self):
        """
        Test get banana
        """
        response = requests.get(API_HOST + '/bananas/1')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_get_banana_not_found(self):
        """
        Test get banana that does not exist
        """
        response = requests.get(API_HOST + '/bananas/-1')
        self.assertEqual(response.status_code, 404)
