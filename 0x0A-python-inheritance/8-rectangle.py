#!/usr/bin/python3
"""Creates a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle.
    Private instance attributes: width and height
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
