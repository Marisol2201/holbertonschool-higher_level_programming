#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
        if idx >= (len(my_list)):
                return(my_list)
        elif idx < 0:
                return(my_list)
        else:
            for element in range(len(my_list)):
                if element == idx:
                    del (my_list[idx])
                    return(my_list)