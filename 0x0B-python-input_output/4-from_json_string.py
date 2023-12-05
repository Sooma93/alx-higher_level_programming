#!/usr/bin/python3
"""
from json to object
"""


import json 


def from_json_string(my_str):
    """
    define function from json to object
    """
    return json.loads(my_str)
