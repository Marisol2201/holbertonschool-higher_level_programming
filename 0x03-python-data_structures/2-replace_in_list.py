#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for element in my_list:
        if idx >= (len(my_list)):
            return(element)
        elif idx < 0:
            return(element)
        else:
            if idx == element - 1:
                return(element)
