#!/usr/bin/python3
"""This class will be the base of all other classes in this project"""
import json
import os
import csv
import pprint


class Base:
    """Base class with object id"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries is "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Returns JSON string representation"""
        with open(cls.__name__ + ".json", 'w', encoding="UTF-8") as myfile:
            mylist = []
            if list_objs is not None:
                for obj in list_objs:
                    mylist.append(obj.to_dictionary())
            myfile.write(cls.to_json_string(mylist))

    @staticmethod
    def from_json_string(json_string):
        """Returns JSON strings in list"""
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attrs already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

        if cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as f:
            content_file = cls.from_json_string(f.read())
        return [cls.create(**dic) for dic in content_file]
