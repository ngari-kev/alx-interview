#!/usr/bin/python3
"""Implementation of Lockboxes"""


def canUnlockAll(boxes):
    """
    checks if all boxes can be opened
    Returns True if possible otherwise False
    """

    unlocked = set([0])
    n = len(boxes)
    keys = set(boxes[0])

    while keys:
        new_key = keys.pop()
        if 0 <= new_key < n and new_key not in unlocked:
            unlocked.add(new_key)
            keys.update(boxes[new_key])
    return len(unlocked) == n
