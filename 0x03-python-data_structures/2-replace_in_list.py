#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (my_list is None) or (idx is None):
        return
    if idx >= (len(my_list)):
            return(element)
    elif idx < 0:
            return(element)
    else:
            my_list[idx] = element
            return(my_list)
