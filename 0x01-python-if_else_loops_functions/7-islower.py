#!/usr/bin/python3
def islower(c):
    ascii_num = ord(c)
    if ascii_num >= 97 and ascii_num <= 112:
        return True
    return False
