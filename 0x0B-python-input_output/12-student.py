#!/usr/bin/python3
"""defines a Student"""


class Student:
    """Public instance attributes:
    first_name
    last_name
    age"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if attrs is None:
            return self.__dict__
        for item in attrs:
            if item in self.__dict__.keys():
                dic[item] = self.__dict__[item]
        return dic
