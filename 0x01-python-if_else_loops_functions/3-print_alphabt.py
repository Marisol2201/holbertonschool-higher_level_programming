#!/usr/bin/python3
for letter in range(97, 123):
    if letter != ord('e') and letter != ord('q'):
        print("{}".format(chr(letter)), end="")
