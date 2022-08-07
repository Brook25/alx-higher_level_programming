#!/usr/bin/python3
"""
This module contains a Class BaseGeometry,
that calculates base gemotry of an object.
"""


class BaseGeometry:
    """Class with methods that calculate the Base Geometry"""
    
    def area(self):
        """Public instance method raises an exception that area is not implementd"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method validates type and value of a variable"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
