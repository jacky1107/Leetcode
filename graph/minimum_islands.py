import math
from typing import List


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","1","1","0"]
]

class Solution:
    def minIslands(self, grid: List[List[str]]) -> int:
        visited = []
        H, W = len(grid), len(grid[0])
        for y in range(H):
            temp = []
            for x in range(W):
                temp.append(0)
            visited.append(temp)

        smallest_size = math.inf
        for y in range(H):
            for x in range(W):
                size = self.explore(grid, y, x, visited, 0)
                if size < smallest_size and size > 0:
                    smallest_size = size

        return smallest_size

    def explore(self, grid, y, x, visited, size):
        H, W = len(grid), len(grid[0])
        row_bound = 0 <= x and x < W
        col_bound = 0 <= y and y < H
        if not row_bound or not col_bound: return size
        if grid[y][x] == "0": return size
        if visited[y][x] == 1: return size

        size += 1
        visited[y][x] = 1
        size = self.explore(grid, y - 1, x, visited, size)
        size = self.explore(grid, y + 1, x, visited, size)
        size = self.explore(grid, y, x - 1, visited, size)
        size = self.explore(grid, y, x + 1, visited, size)
        return size

sol = Solution()
cost = sol.minIslands(grid)
print(cost)
