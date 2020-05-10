#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return None
    int = 0
    for num in range(0, len(roman_string)):
        if num == 0 or dict[roman_string[num]] <= dict[roman_string[num - 1]]:
            int += dict[roman_string[num]]
        else:
            int += dict[roman_string[num]] - 2 * dict[roman_string[num - 1]]
    return int
