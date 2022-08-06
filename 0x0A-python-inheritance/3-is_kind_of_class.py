#!/usr/bin/python3
"""
This Module contains a function that checks if an object is,
of a class whether that class is a parent class or not.
"""


def is_kind_of_class(obj, a_class):
    """Function checks if an object is of a class"""
    return issubclass(type(obj), a_class)
