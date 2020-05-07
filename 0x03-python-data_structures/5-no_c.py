#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    new = list()
    for char in my_string:
        if char != 'c' and char != 'C':
            new.append(char)
    my_string = ''.join(new)
    return(my_string)
