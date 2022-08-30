#!/usr/bin/python3
"""
This Module contains class Square that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """Class square that inherits from rectangle"""
    
    def __init__(self, size):
        """Class initialization function"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns Area of the square"""
        return super().area()

    def __str__(self):
        """Non-formal string representation of the object"""
        return super().__str__()
