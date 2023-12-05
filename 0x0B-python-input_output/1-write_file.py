#!/usr/bin/python3
"""
to write to a file
"""


def write_file(filename="", text=""):
    """
    define how to write file
    """
    with open(filename, "w", encoding='UTF8') as f:
        return f.write(text)
