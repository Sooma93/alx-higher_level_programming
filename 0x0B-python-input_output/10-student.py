#!/usr/bin/python3
"""
json filter
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        define student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
            """
            return dict
            """
            try:
                for attr in attrs:
                    if type(attr) is not str:
                        return self.__dict__
            except Exception:
                return self.__dict__
            my_di = dict()
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_di[key]= value
            return my_di

