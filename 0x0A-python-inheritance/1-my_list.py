#!/usr/bin/python3
"""
This Module contains a class that inherits from List and,
prints a sorted version of it.
"""


class MyList(list):
    """Class that inherits(is a subclass of the built-in list"""
    def print_sorted(self):
        """method sorts integers in a list in ascending order"""
        print(sorted(self.copy()))
