#!/usr/bin/python3
"""
This Module contains a funciton that checks if an object is from a class that,
inherits directly or indirectly from another class.
"""


def inherits_from(obj, a_class):
     """Method for comparing object classes
    Args:
        obj : object to be checked.
        a_class : class to check against.
    Return:
        True if obj isinstance of a_class/ class that inherits from it.
        otherwise False
    """
    if a_class is type(obj):
        return False
    return issubclass(type(obj), a_class)

