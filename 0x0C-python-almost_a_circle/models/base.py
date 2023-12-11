#!/usr/bin/python3
"""
models base class
"""
from json import dumps, loads


class Base:
    """
    represent the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        define the inisiate class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json file dictonary
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        string dictionary
        """
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serializati
        """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """
        instance dictionary
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            i = Rectangle(1, 1)
        elif cls is Square:
            i = Square(1)
        else:
            i = None
        i.update(**dictionary)
        return i
