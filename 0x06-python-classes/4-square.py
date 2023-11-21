#!/usr/bin/python3
"""
define the square class
"""


class Square:
    """
    represent square with private size
    """
    def __init__(self, size=0):
        """
        new instance of square class
        """
        self.size = size

    @property
    def size(self):
        """
        method for retreving the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:

            self.__size = value

    def area(self):
        """
        compute and return value
        """
        return self.__size ** 2
