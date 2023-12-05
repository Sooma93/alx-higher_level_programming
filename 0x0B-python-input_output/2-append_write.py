#!/usr/bin/python3
"""
appened to file
"""


def append_write(filename="", text=""):
    """
    define append file wit utf8
    """
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
