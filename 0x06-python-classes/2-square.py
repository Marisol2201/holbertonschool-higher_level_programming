#!/usr/bin/python3
"""Empty class Square that defines a square"""


class Square:
    """Contains square size"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    pass
