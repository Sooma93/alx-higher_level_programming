#!/usr/bin/python3
"""
load add and save files 
"""


import json
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

arglist = list(sys.argv[1:])

try:
    old_data = load_from_json_file('add_item.json')
except Exception:
    old = []

old.extand(arglist)
save_to_json_file(old_data, "add_item.json")
