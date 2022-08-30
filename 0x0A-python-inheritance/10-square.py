#!/usr/bin/python3
"""
This Module contains Class square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that inherits from rectanlge"""

    def __init__(self, size):
        """Class initialization function"""

        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns Area of the square"""

        return super().area()

    def __str__(self):
        """Non-formal string repr of the object"""

        return super.__str__()
