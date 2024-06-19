#!/usr/bin/python3
"""
This module provides a function to determine the fewest
number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given total.
    Parameters:
    coins (list): A list of integers of values of the coins.
    total (int): The total amount to be achieved.
    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0 or less, returns 0.
         If the total cannot be met by any number of coins, returns -1.
    """
    if total < 1:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        num = total // coin
        total -= num * coin
        count += num

    return count if total == 0 else -1
