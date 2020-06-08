#!/usr/bin/python3
"""This class will be the base of all other classes in this project"""
import json
import os


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
        if list_dictionaries is None or list_dictionaries is "":
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        with open(cls.__name__ + ".json", 'w', encoding="UTF-8") as myfile:
            mylist = []
            if list_objs is not None:
                for obj in list_objs:
                    mylist.append(obj.to_dictionary())
            myfile.write(cls.to_json_string(mylist))
            
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)
    
