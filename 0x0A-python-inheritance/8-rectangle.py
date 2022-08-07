#!/usr/bin/python3
"""
Module contains a Class that inhertis from,
Class BaseGeometry
"""


from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that defines a Rectangle object"""
    
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
