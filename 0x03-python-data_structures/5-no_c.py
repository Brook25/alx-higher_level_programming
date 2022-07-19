#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new = ""
    for i in range(length):
        C = my_string[i]
        if C != 'c' and C != 'C':
            new += my_string[i]
    return new
