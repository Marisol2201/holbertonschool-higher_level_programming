#!/usr/bin/python3
"""unittests for the function def max_integer(list=[])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal_case(self):
        """Tests for the max int at end"""
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_equals_numbers(self):
        """Tests for reapeated numbers"""
        self.assertEqual(max_integer([2, 1, 4, 4, 6, 3, 2]), 6)

    def test_negative_numbers(self):
        """Tests for negative numbers"""
        self.assertEqual(max_integer([2, -5, 4]), 4)

    def test_negative_and_float_numbers(self):
        """Tests for negative and float numbers"""
        self.assertEqual(max_integer([2, -5.3, 4.5]), 4.5)

    def test_1_argument(self):
        """Tests for one argument"""
        self.assertEqual(max_integer([2]), 2)

    def test_None(self):
        """Tests for None argument"""
        self.assertIsNone(max_integer(), None)

    def test_empty_list(self):
        """Tests for empty list"""
        self.assertEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
