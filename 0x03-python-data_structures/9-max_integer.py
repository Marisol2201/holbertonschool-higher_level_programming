#!/usr/bin/python3
def max_integer(my_list=[]):
    if (my_list is None) or (len(my_list) < 1):
        return (None)
    big = 0
    for num in my_list:
        if num > big:
            big = num
    return (big)
