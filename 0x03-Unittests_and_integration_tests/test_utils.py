#!/usr/bin/env python3
"""Parameterize a unit test"""
import requests
from functools import wraps
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """ testing access to nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path, expectedOutput):
        self.assertEqual(access_nested_map( nested_map, path), expectedOutput)
        
if __name__ == '__main__':
    unittest.main()
              