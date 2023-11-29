#!/usr/bin/python3
"""
adding two numbers
"""


def add_integer(a, b=98):
    """
    add two integar
    a: first int
    b: seconed
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
