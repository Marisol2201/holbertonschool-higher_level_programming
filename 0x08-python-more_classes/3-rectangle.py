#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width is 0 or self.__height is 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        string = ""
        if self.__width > 0 and self.__height > 0:
            for x in range(self.__height):
                string += "\n"
                for z in range(self.__width):
                    string += "#"
            return string[1:]