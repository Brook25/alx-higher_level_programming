#!/usr/bin/python3
"""
This Module contains class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Class square that inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area method that returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """string representation of the area"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
