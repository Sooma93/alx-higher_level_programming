#!/usr/bin/python3
"""
save json file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    write object to text file
    """
    with open(filename, "w", encoding="UTF8") as f:
        json.dump(my_obj, f)
