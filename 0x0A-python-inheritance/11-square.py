#!/usr/bin/python3
"""
This module contains Class square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectnagle"""

    def __init__(self, size)
    """Initializer function for square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Funciton returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        "string representation of the instance"""
        return "[Square]{}/{}".format(self.__size, self.__size)
