#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for value in a_dictionary:
        new[value] = a_dictionary[value] * 2
    return new
