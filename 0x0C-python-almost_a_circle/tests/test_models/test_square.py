"""Unittest for square.py"""


import unittest
from models.square import Square

class Test_square(unittest.TestCase):
    
    def test_square_noargs(self):
        self.assertRaises(TypeError, Square)
        
    def test_square_noargs(self):
        self.assertRaises(TypeError, Square)