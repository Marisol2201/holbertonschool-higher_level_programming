#!/usr/bin/python3
"""Unittest for square.py"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class Test_square(unittest.TestCase):
    """Testing Square"""

    def SetOut(self):
        Base._Base__nb_objects = 0

    def test_size_float(self):
        with self.assertRaises(TypeError):
            Square(2.5, 8, 3, 4)

    def test_normal_Square(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 2)
        with self.assertRaises(TypeError) as cm:
            s1 = Square()

        s2 = Square(3, 3)
        self.assertEqual(s2.area(), 9)
        self.assertEqual(s2.width, 3)
        self.assertEqual(s2.height, 3)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.id, 3)

        s3 = Square(7, 2, 7)
        self.assertEqual(s3.area(), 49)
        self.assertEqual(s3.width, 7)
        self.assertEqual(s3.height, 7)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 7)
        self.assertEqual(s3.id, 4)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.area(), 1)
        self.assertEqual(s4.width, 1)
        self.assertEqual(s4.height, 1)
        self.assertEqual(s4.x, 2)
        self.assertEqual(s4.y, 3)
        self.assertEqual(s4.id, 4)
        with self.assertRaises(TypeError) as cm:
            s1 = Square(1, 2, 3, 4, 5)

    def test_Square_exceptions(self):
        with self.assertRaises(TypeError) as cm:
            Square("hi", 10, 10, 10)
        self.assertTrue("width must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, {"hi"}, 10, 10)
        self.assertTrue("x must be an integer" in str(cm.exception))
        with self.assertRaises(TypeError) as cm:
            Square(10, 10, ["hi"], 10)
        self.assertTrue("y must be an integer" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Square(-5, 10, 10, 10)
        self.assertTrue("width must be > 0" in str(cm.exception))
        with self.assertRaises(ValueError) as cm:
            Square(0, 10, 10, 10)

    def test_display(self):
        r = Square(1, 1)
        display_example = " #\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            r.display()
        self.assertEqual(fakeOutput.getvalue(), display_example)

        s = Square(3, 2, 2, 1)
        display_exmp = "\n\n  ###\n  ###\n  ###\n"
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            s.display()
        self.assertEqual(fakeOutput.getvalue(), display_exmp)
