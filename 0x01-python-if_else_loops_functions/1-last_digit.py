#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
msn = "Last digit of"
msn_less = "and is less than 6 and not 0"

if number < 0:
    last = last * -1

if last > 5:
    print("{} {:d} is {:d} and is greater than 5".format(msn, number, last))
elif last == 0:
    print("{} {:d} is {:d} and is 0".format(msn, number, last))
else:
    print("{} {:d} is {:d} {}".format(msn, number, last, msn_less))
