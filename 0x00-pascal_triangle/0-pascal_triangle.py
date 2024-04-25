#!/usr/bin/python3
"""
Generate Pascal's triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for col in range(1, n):
        row = [1]
        for j in range(1, col):
            value = pascal[col - 1][j - 1] + pascal[col - 1][j]
            row.append(value)
        row.append(1)
        pascal.append(row)

    return pascal
