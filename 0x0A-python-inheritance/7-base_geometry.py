#!/usr/bin/python3
"""
This module contains a Class.
BaseGeometry.
"""


class BaseGeometry:
    """Class with public instance methods."""

    def area(self):
        """Raises an exception."""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validates type, value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
