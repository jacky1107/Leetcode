from copy import copy
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H, W = len(grid), len(grid[0])

        visited = []
        for y in range(H):
            temp = []
            for x in range(W):
                temp.append(0)
            visited.append(temp)

        cost = 0
        for y in range(H):
            for x in range(W):
                if grid[y][x] == "1" and visited[y][x] == 0:
                    self.dfs2(grid, visited, (y, x))
                    cost += 1

        return cost

    def dfs(self, grid, visited, corr):
        H, W = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # find the neighboring node then visit each node to check whether it is "1" or not
        # also check the node whether is visited.
        for dir in dirs:
            dy = corr[0] + dir[0]
            dx = corr[1] + dir[1]
            if (0 <= dy and dy < H and 0 <= dx and dx < W and visited[dy][dx] == 0 and grid[dy][dx] == "1"):
                visited[dy][dx] = 1
                self.dfs(grid, visited, (dy, dx))


    def dfs2(self, grid, visited, corr):
        dy = corr[0]
        dx = corr[1]
        H, W = len(grid), len(grid[0])
        if (0 > dy or dy >= H or 0 > dx or dx >= W or visited[dy][dx] == 1 or grid[dy][dx] == "0"):
            return
        visited[dy][dx] = 1
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # find the neighboring node then visit each node to check whether it is "1" or not
        # also check the node whether is visited.
        for dir in dirs:
            dy = corr[0] + dir[0]
            dx = corr[1] + dir[1]
            self.dfs2(grid, visited, (dy, dx))



grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
sol = Solution()
cost = sol.numIslands(grid)
print(cost)