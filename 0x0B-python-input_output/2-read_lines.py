#!/usr/bin/python3
"""reads n lines of a text file (UTF8) and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """func that reads n lines of a text file (UTF8) & prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end="")
