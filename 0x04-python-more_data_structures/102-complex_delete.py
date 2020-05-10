#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if key in a_dictionary and key is not "":
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return a_dictionary
