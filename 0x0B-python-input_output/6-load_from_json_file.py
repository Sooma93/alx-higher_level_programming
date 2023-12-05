#!/usr/bin/python3
"""
creat object from json file
"""


import json


def load_from_json_file(filename):
    """
    define load from json file
    """
    with open(filename, "r" encoding"UTF8") as f:
        return json.load(f)
