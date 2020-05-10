#!/usr/bin/python3
def roman_to_int(roman_string):
    '''
    num -1 (si hay 2 letras, la primera letra)
    '''
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    int = 0
    temp = roman_string
    for num in range(len(temp)):
        if num > 0 and dict[temp[num]] > dict[temp[num - 1]]:
            int += dict[temp[num]] - 2 * dict[temp[num - 1]]
        else:
            int += dict[temp[num]]
    return int
