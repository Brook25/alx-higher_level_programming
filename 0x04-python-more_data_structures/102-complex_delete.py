#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    b_dictionary = a_dictionary.copy()
    for key, val in b_dictionary.items():
        if value == val:
            del a_dictionary[key]
    b_dictionary.clear()
    return a_dictionary
