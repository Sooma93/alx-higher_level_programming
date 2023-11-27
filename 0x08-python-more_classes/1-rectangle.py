#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    rectangle class with widith and heght
    """
    def __init__(self, width=0, height=0):
        """
        inisiat rectangle with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter to width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the value of height of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
