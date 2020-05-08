#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for idx in my_list:
        if idx == search:
            new.append(replace)
        else:
            new.append(idx)
    return(new)
