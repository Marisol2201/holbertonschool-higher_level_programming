#!/usr/bin/python3
for num in range(1, 90):
    last = num % 10
    penultimate = int(num / 10)
    if penultimate == 8 and last == 9:
        print(89)
    elif penultimate < last:
        print("{:d}{:d}".format(penultimate, last), end=", ")
