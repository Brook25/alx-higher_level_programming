#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in b_dictionary.copy().items():
        if value == val:
            del a_dictionary[key]
    return a_dictionary
