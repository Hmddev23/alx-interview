#!/usr/bin/python3
"""
This script contains a function to
rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list of list of int): A 2D list of integers.
    Returns:
        None: The function modifies the matrix in-place.
    """
    size = len(matrix)

    for row in range(size):
        for col in range(row, size):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    for row in range(size):
        matrix[row] = matrix[row][::-1]
