#!/usr/bin/python3
"""
This module contains a Class BaseGeometry,
that calculates base gemotry of an object.
"""


class BaseGeometry:
    """Class with methods that calculate Base Geometry"""

    def area(self):
        """Public instance method raises a specific exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method validates type and value of variable"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle that defines a Rectangle object"""
    
    def __init__(self, width, height):
        self.integer_validator('width', width)    
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
