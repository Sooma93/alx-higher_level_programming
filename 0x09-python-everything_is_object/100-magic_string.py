#!/usr/bin/python3
def magic_string():
    magic_string.con = getattr(magic_string, "con", 0) + 1
    return ", ".join(["BestSchool" for s in range(magic_string.con)])
