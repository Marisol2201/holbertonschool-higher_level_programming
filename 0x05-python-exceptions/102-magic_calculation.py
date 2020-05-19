#!/usr/bin/python3
def magic_calculation(a, b):
    '''
    += implace add
    setup_except = try:
    '''
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except:
            result = a + b
    return result
