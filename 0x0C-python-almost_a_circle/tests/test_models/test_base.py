#!/usr/bin/python3
"""Unittest for base.py"""


import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing Base"""

    def SetUp(self):
        """factor out set-up code and which the testing framework will
        automatically call for every single test we run"""
        Base._Base__nb_objects = 0
        
    def tearDown(self):
        """Resets the Base Class for the module
        method that tidies up after the test method has been run
        will be run whether the test method succeeded or not"""
        Base._Base__nb_objects = 0
        
    def test_rectangle_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test_normal_case(self):
        """normal cases"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_zero(self):
        """zero number test"""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    def test_negatives(self):
        """negative numbers test"""
        b1 = Base(-5)
        self.assertEqual(b1.id, -5)
        
    def test_to_and_from_json_string_square(self):
        """ Test to_and_from_json_string"""
        r1 = Square(6, 6, 6)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
