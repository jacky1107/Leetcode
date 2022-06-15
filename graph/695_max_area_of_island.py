from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = []
        H, W = len(grid), len(grid[0])
        for y in range(H):
            temp = []
            for x in range(W):
                temp.append(0)
            visited.append(temp)
        
        largest = 0
        for y in range(H):
            for x in range(W):
                size = self.explore(grid, y, x, visited, 0)
                if size > largest:
                    largest = size
        
        return largest
    
    def explore(self, grid, y, x, visited, size):
        H, W = len(grid), len(grid[0])
        row_boundary = 0 <= x and x < W
        col_boundary = 0 <= y and y < H
        if not row_boundary or not col_boundary: return size
        if grid[y][x] == 0: return size
        if visited[y][x] == 1: return size

        visited[y][x] = 1
        size += 1
        size = self.explore(grid, y - 1, x, visited, size)
        size = self.explore(grid, y + 1, x, visited, size)
        size = self.explore(grid, y, x - 1, visited, size)
        size = self.explore(grid, y, x + 1, visited, size)
        return size


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
size = sol.maxAreaOfIsland(grid)
print(size)
