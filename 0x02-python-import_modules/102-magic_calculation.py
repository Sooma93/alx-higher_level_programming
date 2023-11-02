#!/usr/bin/python3def
magic_calculation(a, b):
    from magic_calculation_12 import add, sub
    if a < b:
        i = add(a, b)
        for c in range(4, 6):
            i = add(i, c)
        return i
    else:
        return sub(a, b)
    return 0
