#!/usr/bin/python3
"""
the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        the super part
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        defintion of string in the square class
        """
        return '[{}] ({}) {}/{} - {}'.format(
                type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update the args and kwargs values
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns the dictionary representation of a Square
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
