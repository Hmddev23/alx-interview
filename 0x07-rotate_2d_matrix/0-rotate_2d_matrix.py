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

    for i in range(size):
        for j in range(i, size):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(size):
        matrix[i] = matrix[i][::-1]
