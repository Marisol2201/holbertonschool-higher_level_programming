#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for key in a_dictionary:
        key = max(a_dictionary.keys(), default=None)
        return(key)
