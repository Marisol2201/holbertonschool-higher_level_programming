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
        """Constructor of the class, id is optional"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
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
        """Returns an instance with all attributes already set"""
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
        """Returns a list of instances of the called class"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, mode="r", encoding="utf-8") as f:
            content_file = cls.from_json_string(f.read())
        return [cls.create(**dic) for dic in content_file]
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file"""
        res = [item.to_dictionary() for item in list_objs]
        with open(cls.__name__ + ".csv", mode="w") as save_file:
            write_to = csv.DictWriter(save_file, res[0].keys())
            write_to.writeheader()
            write_to.writerows(res)
            
    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        result = []
        result_dictionary = {}
        with open(cls.__name__ + ".csv", mode="r") as read_file:
            read_from = csv.DictReader(read_file)
            for item in read_from:
                for key, value in dict(item).items():
                    result_dictionary[key] = int(value)
                result.append(cls.create(**result_dictionary))
        return result
