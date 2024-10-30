#!/usr/bin/python3
"""A script checking the least number of iterations needed"""


def minOperations(n):
    """
    calculates the fewest number of operations
    needed to result in exactly n H characters in a file.
    """
    if not isinstance(n, int):
        return 0
    least_factor = 2
    if n < 2:
        return 0
    while least_factor < n + 1:
        if n % least_factor == 0:
            operations = least_factor
            return minOperations(n // least_factor) + operations
        least_factor = least_factor + 1
