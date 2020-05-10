#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    result = 0.0
    mul = tuple([x * y for x, y in my_list[:]])
    num2 = tuple([y for x, y in my_list[:]])
    result = sum(mul[:]) / sum(num2[:])
    return(result)
