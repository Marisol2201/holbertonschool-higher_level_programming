#!/usr/bin/python3
"""returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    """f is file object"""
    with open(filename, encoding='utf-8') as f:
        return len(f.readlines())
