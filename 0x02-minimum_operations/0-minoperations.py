#!/usr/bin/python3
"""
project: 0-minoperations.
Module for calculating the fewest number of operations
needed to result in exactly n H characters.
"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters

    minOperations: calculate the fewest number of operations
    needed to result in exactly n H characters.
    Parameters:
        n (int): The target number of H characters.
    Returns:
        int: The number of operations needed to achieve
        n H characters, or 0 if it's impossible.
    """
    if n < 2:
        return 0

    operations, div = 0, 2

    while div <= n:
        if n % div == 0:
            operations += div
            n = n / div
            div -= 1
        div += 1

    return operations
