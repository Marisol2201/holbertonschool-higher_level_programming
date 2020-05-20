#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Contains square size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for x in range(self.__position[1]):
                print("")
        for y in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        string = ""
        if self.__size:
            for x in range(self.__position[1]):
                string += '\n'
            for x in range(self.__size):
                for k in range(self.__position[0]):
                    string += " "
                for j in range(self.__size):
                    string += "#"
                if (x + 1) != self.__size:
                    string += '\n'
        return string
