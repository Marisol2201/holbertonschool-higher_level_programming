#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


"""use your function load_from_json_file from 8-load_from_json_file.py"""
filename = "add_item.json"
if os.path.isfile(filename):
    new_list = load_from_json_file(filename)
    new_list += sys.argv[1:]
    save_to_json_file(list(new_list), filename)
else:
    save_to_json_file(list(sys.argv[1:]), filename)
