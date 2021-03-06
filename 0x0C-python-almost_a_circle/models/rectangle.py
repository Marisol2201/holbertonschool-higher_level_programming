#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base
import sys


class Rectangle(Base):
    """inherits from Base, new rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for new class, optional x, y args and id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Setter and getters for the Rectangle instance attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Setter and getters for the Rectangle instance attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Setter and getters for the Rectangle instance attributes"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Setter and getters for the Rectangle instance attributes"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Returns printed rectangle with '#'
        y is newline, x is space"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(self.x * " ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns formatted information display"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            str(self.id),
            str(self.x),
            str(self.y),
            str(self.width),
            str(self.height)))

    def update(self, *args, **kwargs):
        """Updates rectangle values"""
        if args is None or not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        elif len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

    def to_dictionary(self):
        """Returns dict representation"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
