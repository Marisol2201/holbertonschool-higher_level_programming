#!/usr/bin/python3
def element_at(my_list, idx):
    for element in my_list:
        if idx > (len(my_list)):
            return("")
        elif idx < 0:
            return("")
        else:
            if idx == element - 1:
                return(element)
