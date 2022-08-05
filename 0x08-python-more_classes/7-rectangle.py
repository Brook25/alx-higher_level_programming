#!/usr/bin/python3
"""
This Module defines a Printable Rectangle.
"""


class Rectangle:
    """Class Rectangle"""
    
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property checker for Height attribute"""
        return self.__width

    @height.setter
    def width(self, value):
        """Sets height of Rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property checker for attribute width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Public instance attribute returns area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance perimeter returns perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """string representation of the object"""
        if self.__height == 0 or self.__width == 0:
            return ""
        out_put = (f"{self.print_symbol}" * self.__width + '\n') * self.__height
        return out_put[:-1]

    def __repr__(self):
        """Returns string representation of an object to recreate the object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
