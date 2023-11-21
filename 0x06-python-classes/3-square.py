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
        new instance of square size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        copmute and return area of square
        """
        return self.__size ** 2
