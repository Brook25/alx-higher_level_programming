#!/usr/bin/python3
"""
This Module contains a function that checks if an object is an instance of,
a given Class.
"""


def is_same_class(obj, a_class):
    """Function to check if an object is an instance of a Class"""
    if issubclass(object, a_class):
        return isinstance(obj, a_class)
