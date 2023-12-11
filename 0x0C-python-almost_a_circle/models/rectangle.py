#!/usr/bin/python3
"""
to my first Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        define the initiotion of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """
        height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """
        the x value
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """
        th ey value
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """
        validition value
        """
        if type(value) != integer:
            raise TypeError("{}  must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be > 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """
        calculate the area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        to display the rectangle
        """
        s = "\n" * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end="")

    def __str__(self):
        """
        define the string
        """
        return '[{}] ({}) {}/{} - {}/{}'.format(type(
                self).__name__, self.id, self.x, self.y,
                self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """
        update method using args
        """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """
        use args and kwargs
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """
            returns the dictionary repr of a rect
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
