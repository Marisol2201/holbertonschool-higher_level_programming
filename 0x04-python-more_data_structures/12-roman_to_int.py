#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None:
        return 0
    if type(roman_string) is str:
        int = 0
        for n in range(0, len(roman_string)):
            if n == 0 or dict[roman_string[n]] <= dict[roman_string[n - 1]]:
                int += dict[roman_string[n]]
            else:
                int += dict[roman_string[n]] - 2 * dict[roman_string[n - 1]]
        return int
