#!/usr/bin/python3

"""
    finding the perimeter of an island.
"""


def island_perimeter(grid):
    """
        returns the perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, columns = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
