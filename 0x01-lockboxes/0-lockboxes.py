#!/usr/bin/python3
"""
determine if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    determine if all the boxes can be opened.

    Args:
        boxes (list of lists): A list of lists where each inner
        list represents a box, and the indices of the outer list
        represent the box numbers.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    nbr_boxes = len(boxes)
    key_pairs = [0]
    ctr = 0
    pointer = 0

    while pointer < len(key_pairs):
        key = key_pairs[pointer]
        for key in boxes[key]:
            if 0 < key < nbr_boxes and key not in key_pairs:
                key_pairs.append(key)
                ctr += 1
        pointer += 1

    return ctr == nbr_boxes - 1
