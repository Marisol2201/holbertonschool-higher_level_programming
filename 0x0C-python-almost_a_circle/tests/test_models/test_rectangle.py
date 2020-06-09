#!/usr/bin/python3
"""Unittest for rectangle.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class Test_rectangle(unittest.TestCase):
    """Testing Rectangle"""

    def SetOut(self):
        Base._Base__nb_objects = 0

    def test_normal_case(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r2.id, 7)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_size_float(self):
        with self.assertRaises(TypeError):
            Rectangle(2.5, 8, 3, 4)

    def test_different_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_validate_integer(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle("hi", 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, False, 10, 10)
        self.assertTrue("height must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, {"hi", 0}, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle(10, 10, 10, (2,))
        self.assertTrue("y must be an integer" in str(cm.exception))

    def test_integer_empty(self):
        with self.assertRaises(TypeError) as cm:
            Rectangle([], 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Rectangle({}, 10, 10, 10)

    def test_checks_value(self):
        with self.assertRaises(ValueError) as cm:
            Rectangle(-5, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Rectangle(0, 10, 10, 10)

    def test_area(self):
        r1 = Rectangle(10, 10, 0, 0, 10)
        self.assertEqual(r1.area(), 100)
        with self.assertRaises(TypeError):
            r1.area(10)

    def test_display(self):
        r = Rectangle(1, 1)
        display_example = "#\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)

        r301 = Rectangle(3, 2, 2, 1, 301)
        display_exmp = "\n  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r301.display()
        self.assertEqual(fakeOutput.getvalue(), display_exmp)
