#!/usr/bin/python3
"""
Contains the definition of the function lookup
"""


def lookup(obj):
    """Returns list of attributes and methods of an object"""

    return list(dir(obj))
