#!/usr/bin/python3
"""writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """fun that writes an Object to a text file, using a JSON representation"""
    with open(filename, encoding='utf-8', mode='w+') as f:
        return f.write(json.dumps(my_obj))
