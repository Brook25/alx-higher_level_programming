#!/usr/bin/python3
"""
Contains the definiton for the class MyList that inherits from list.
"""


class MyList(list):
    """definiton for Class MyList that inherits from list.
    """
    def print_sorted(self):
        """Prints list elements(int) in ascending order"""

        sortedlist = sorted(self)
        print(sortedlist)
