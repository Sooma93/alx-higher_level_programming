#!/usr/bin/python3
"""
rectangle class
"""


class Rectangle:
    """
    rectangle class with widith and heght
    """
    number_of_instances = 0
    """
    number of active instance
    """
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        inisiat rectangle with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        calculate the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the return parameter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        return rpresntve
        """
        if not self.width or not self.height:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """
        return reproduction
        """
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """
        type delete message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
