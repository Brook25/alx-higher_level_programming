#!/usr/bin/python3
"""
This Module contains a function that checks if an object is an instance of,
a given Class.
"""


def is_same_class(obj, a_class):
    """Function to check if an object is an instance of a Class"""
    if type(obj) is a_class:
        return True
    else:
        return False
