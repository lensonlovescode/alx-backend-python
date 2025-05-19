#!/usr/bin/env python3
"""
Unit test for access_nested_map function
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class to test access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test case for access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Tests that keyError is raised if the key in the tuple is not found
        """
        with self.assertRaises(KeyError):
            access_nested_map((nested_map, path), expected)


class TestGetJson(unittest.TestCase):
    """
    Test class for mocking an API call
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        test that the api call returns a json object
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            payload = get_json(test_url)
            self.assertEqual(payload, test_payload)
