#!/usr/bin/python3
"""
only is needed argv module from sys
length = quantity of arguments
(length - 1) //without argument 0
for arg in range(1, length) //arg = argv position >0'
    """
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print("0 arguments.")
    elif length == 2:
        print("1 argument:\n1: {:s}".format(argv[1]))
    else:
        print("{:d} arguments:".format(length - 1))
        for arg in range(1, length):
            print("{:d}: {:s}".format(arg, argv[arg]))
