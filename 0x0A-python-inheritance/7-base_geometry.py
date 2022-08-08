#!/usr/bin/python3
"""
This module contains a Class BaseGeometry,
that calculates base gemotry of an object.
"""


class BaseGeometry:
    """Class with methods that calculate Base Geometry"""
    
    def area(self):
        """Public instance method raises an exception"""
        
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Public instance method validates type, value"""
        
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

