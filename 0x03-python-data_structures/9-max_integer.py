#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is "":
        return
    grande = 0
    for numero in my_list:
        if numero > grande:
            grande = numero
    return grande
