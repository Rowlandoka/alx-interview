#!/usr/bin/python3
"""
island_perimeter: Return the perimeter of a grid
"""


def island_perimeter(grid):
    """
    Return perimeter of a grid
    """
    m = len(grid)
    n = len(grid[0])

    island = 0
    neighbour = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                island += 1
                if i + 1 < m and grid[i + 1][j] == 1:
                    neighbour += 1
                if j + 1 < n and grid[j + 1][i] == 1:
                    neighbour += 1
    return island * 4 - neighbour * 2
