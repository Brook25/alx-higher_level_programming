'''
Creates empty class
'''

class Square:
    ''' A class that defines square objects '''
    def __init__(self, size=0):
    ''' Initializes an object with size instance attribute '''
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
