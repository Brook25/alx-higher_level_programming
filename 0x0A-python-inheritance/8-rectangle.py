#!/usr/bin/python3
"""
This module contains a Class BaseGeometry,
that calculates base gemotry of an object.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that defines a Rectangle object"""
    
    def __init__(self, width, height):
        self.integer_validator('width', width)    
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
