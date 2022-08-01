#!/usr/bin/python3
"""
Contains the definition of the function lookup
"""


def lookup(obj):
    """Returns list of attributes and methods of an object
    Args:
        obj (any): the object whose attributes and methods are to be returned
    """

    return (dir(obj))
