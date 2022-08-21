#!/usr/bin/python3
"""
This Module contains class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method implements area"""
        return self.__width * self.__height

    def __str__(self):
        """builtin method prints string rep"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
