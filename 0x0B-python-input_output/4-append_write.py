#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added"""
    """the + char ('a+') is for read too"""
    with open(filename, encoding='utf-8', mode='a+') as f:
        return f.write(text)
