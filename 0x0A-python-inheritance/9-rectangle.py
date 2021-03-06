#!/usr/bin/python3
"""Creates a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with Private instance attributes:
    - width and height
    Public method area()
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return str("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        return self.__height * self.__width
