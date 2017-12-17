"""
Tests for version resource
"""

from unittest import TestCase

import requests

from tests.resources import API_HOST


class TestVersion(TestCase):
    """
    Tests for version resource
    """
    def test_version(self):
        """
        Test get version
        """
        response = requests.get(API_HOST + '/version')
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.json().get('version'), r'\d+\.\d+')
