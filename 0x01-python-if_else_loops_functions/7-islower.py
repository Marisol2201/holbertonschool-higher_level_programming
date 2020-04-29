#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c < ord('a') or c > ord('z'):
            return False
    else:
        return True
