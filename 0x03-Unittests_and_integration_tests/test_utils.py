#!/usr/bin/env python3
""" Parameterize a unit test
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    This class inherits from unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test access_nested_map method to test that the method returns
        what it is supposed to.
        Args:
            nested_map(Dict): dictonary
            path(List, tuple, set): keys to get value in nested decorators
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test access_nested_map_exception the `assertRaises` context manager to
        test that a `KeyError` is raised for the following inputs.
        Args:
            nested_map(Dict): dictonary
            path(List, Tuple, set): keys to get value of nested decorators
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    This class implements the TestGetJson.test_get_json method to test that
    `utils.get_json` returns the expected result.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Tests that the output of get_json is equal to test_payload
        Args:
            test_url: url to send http request
            test_payload: payload to test
            mock_requests_get: expected json response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    This class implements the `TestMemoize(unittest.TestCase)`
    class with a test_memoize method.
    """
    def test_memoize(self):
        """
        Tests that when calling a_property twice, the correct result is
        returned but `a_method` is only called once using `assert_called_once`
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_obj:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_obj.assert_called_once()
