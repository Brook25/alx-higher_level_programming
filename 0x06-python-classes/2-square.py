#!/usr/bin/python3
"""
Class Square: Defines a square
"""

class Square:
    """ A Class that defines square objects """
    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError
        except TypeError:
            print("size must be an integer", end="")
            raise
        try:
            if size < 0:
                raise ValueError
        except ValueError:
            print("size must be >= 0", end="")
            raise
        else:
            self.__size = size
