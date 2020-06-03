#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8) and returns the
     number of characters written"""
    """the ('w+') char is for read too"""
    with open(filename, encoding='utf-8', mode='w+') as f:
        return f.write(text)
