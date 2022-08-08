#!/usr/bin/python3
"""
This Module contains a funciton checks if an object is from a class
that inherits directly or indirectly from another class.
"""


def inherits_from(obj, a_class):
     """Method to compare object classes"""
    
    if a_class is type(obj):
        return False
    return issubclass(type(obj), a_class)

