#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) != 0:
        return(max(list_of_integers))
