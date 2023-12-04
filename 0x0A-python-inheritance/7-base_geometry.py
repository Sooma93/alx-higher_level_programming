#!/usr/bin/python3
"""
basegemotry class
"""


class BaseGeometry:
    """
    basegemotry class
    """
    def area(self):
        """
        calculate area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        valdition value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
