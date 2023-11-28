#!/usr/bin/python3
"""
print my name
"""


def say_my_name(first_name, last_name=""):
    """
    print my first name and last
    Args:
        first_name (str): first name to print
        last_name (str): last name to print
    Raises:first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
