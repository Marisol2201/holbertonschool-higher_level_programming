"""Unittest for rectangle.py"""


import unittest
from models.rectangle import Rectangle

class Test_rectangle(unittest.TestCase):


    def test_rectangle_noargs(self):
        self.assertRaises(TypeError, Rectangle)