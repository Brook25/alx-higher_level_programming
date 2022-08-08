#!/usr/bin/python3
"""
This Module contains a funciton that checks if an object is from a class that,
inherits directly or indirectly from another class.
"""


def inherits_from(obj, a_class):
    """Function checks if an object is an instance of a calss that inherits from another class"""
    if a_class is not obj:
        return issubclass(type(obj), a_class)

