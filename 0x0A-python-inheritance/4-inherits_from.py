#!/usr/bin/python3
"""
This Module contains a funciton that checks if an object is from a class that,
inherits directly or indirectly from another class.
"""


def inherits_from(obj, a_class):
    """Function checks if an object of a class is inherited"""
    if a_class is not obj:
        return False
    return issubclass(type(obj), a_class)

