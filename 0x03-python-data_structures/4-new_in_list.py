#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return
    if idx >= (len(my_list)):
            return(my_list)
    elif idx < 0:
            return(my_list)
    else:
            my_list[idx] = element
            return(my_list)
