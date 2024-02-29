#!/usr/bin/python3
"""
write alogrthem for list of int
"""
def find_peak(list_of_integers):
    """
    find a peak in list of int
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
