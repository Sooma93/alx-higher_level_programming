#!/usr/bin/python3
"""
pascal trangle
"""


def pascal_triangle(n):
    """
    define pascal trangle
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tringle = tri[-1]
        i = [1]
        for r in range(len(tringle) - 1):
            i.append(tringle[r] + tringle[r + 1])
        i.append(1)
        tri.append(i)
    return tri
