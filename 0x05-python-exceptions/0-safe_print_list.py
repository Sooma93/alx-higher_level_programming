#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    e = 0
    try:
        while e is not x:
            print(my_list[e], end=' ')
            e += 1
    except IndexError:
        none
        print()
        return e
