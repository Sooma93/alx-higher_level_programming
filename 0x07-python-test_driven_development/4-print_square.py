#!/usr/bin/python3
"""
square printing function
"""


def print_square(size):
    """
    print square with # char

    Args:
    size (int): the height andwidth of square
    Raises:
        TypeError: if size not integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
