#!/usr/bin/python3
"""
Module contains the method to check if a class of an object,
inherits from another class
"""


def inherits_from(obj, a_class):
    """Method compares if an object class inherits from another class"""

    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
