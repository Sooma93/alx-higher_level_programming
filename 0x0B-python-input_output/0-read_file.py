#!/usr/bin/python3
"""
function to read file
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, encoding='UTF8') as f:
        print(f.read(), end="")
