#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 != 0:
        lower_c = chr(letter - 32)
        print("{}".format(lower_c), end="")
    else:
        print("{}".format(chr(letter)), end="")
