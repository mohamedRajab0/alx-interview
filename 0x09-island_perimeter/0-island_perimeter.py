#!/usr/bin/python3
"""
island perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.
    The grid is a list of lists where:
    - 0 represents water
    - 1 represents land
    The function uses Depth-First Search (DFS) to traverse the island
    and calculate its perimeter.
    Args:
        grid (List[List[int]]): A 2D list representing the grid.
    Returns:
        int: The perimeter of the island.
    Example:
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        island_perimeter(grid)  # Returns 16
    """
    visited = set()

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 1
        elif grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        perimeter = dfs(i + 1, j)
        perimeter += dfs(i - 1, j)
        perimeter += dfs(i, j + 1)
        perimeter += dfs(i, j - 1)
        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)
    return 0
