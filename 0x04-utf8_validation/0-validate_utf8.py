#!/usr/bin/python3
"""
define a function to validate if a given list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    check if the input list of integers represents a valid UTF-8 encoding.
    Args:
    data: List of integers where each integer represents a byte (0-255).
    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for i in data:
        leading_bit_mask = 1 << 7
        if num_bytes == 0:
            while leading_bit_mask & i:
                num_bytes += 1
                leading_bit_mask = leading_bit_mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            if not (i & mask1 and not (i & mask2)):
                    return False

        num_bytes -= 1

    if num_bytes == 0:
        return True

    return False
