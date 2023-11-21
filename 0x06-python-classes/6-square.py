#!/usr/bin/python3
"""
define the square class
"""


class Square:
    """
    represent square with private size
    """
    def __init__(self, size=0, position=(0, 0)):
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

    @property
    def position(self):
        """
        method for retriving postion
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        method setting postion
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int)
                and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__postion = value

    def area(self):
        """
        compute and return value
        """
        return self.__size ** 2

    def my_print(self):
        """
        print the square using #
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.__postion[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
