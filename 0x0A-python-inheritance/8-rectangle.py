#!/usr/bin/python3
"""
rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    subclass rectangle
    """
    def __init__(self, width, height):
        """
        calculate
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
