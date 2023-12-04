#!/usr/bin/python3
"""
define sub class
"""


def inherits_from(obj, a_class):
    """
    if its sub class or not
    """
    return isinstance(obj, a_class) and type(obj) != a_class
