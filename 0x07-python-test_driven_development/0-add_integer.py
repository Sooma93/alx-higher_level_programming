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
    return int(a) + int(b)
    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
