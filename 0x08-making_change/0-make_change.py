#!/usr/bin/python3
"""Calculates the fewest number of coins needed
to meet a given total.
"""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed
    to meet a given total.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        coin_count += total // coin
        total %= coin

    if total != 0:
        return -1

    return coin_count
