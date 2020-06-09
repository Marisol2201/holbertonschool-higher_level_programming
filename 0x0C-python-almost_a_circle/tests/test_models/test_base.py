#!/usr/bin/python3
"""Unittest for base.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Testing Base"""

    def SetOut(self):
        """factor out set-up code and which the testing framework will
        automatically call for every single test we run"""
        Base._Base__nb_objects = 0

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
