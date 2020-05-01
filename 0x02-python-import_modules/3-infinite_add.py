#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 0:
        print("0")
    else:
        result = 0
        for count in range(1, len(argv)):
            result = result + int(argv[count])
        print("{}".format(result))
