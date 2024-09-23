from typing import List
import collections

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]

        for y in range(m):
            memo[y][0] = 1

        for x in range(n):
            memo[0][x] = 1

        for y in range(1, m):
            for x in range(1, n):
                memo[y][x] = memo[y - 1][x] + memo[y][x - 1]
        return memo[m-1][n-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        H, W = len(obstacleGrid), len(obstacleGrid[0])
        memo = [[1] * W for _ in range(H)]
        
        for y in range(H):
            if obstacleGrid[y][0] == 1: memo[y][0] = 0
            else: memo[y][0] = memo[y-1][0]

        for x in range(W):
            if obstacleGrid[0][x] == 1: memo[0][x] = 0
            else: memo[0][x] = memo[0][x-1]

        for y in range(1, H):
            for x in range(1, W):
                if obstacleGrid[y][x] == 1: memo[y][x] = 0
                else: memo[y][x] = memo[y-1][x] + memo[y][x-1]

        return memo[H-1][W-1]

m = 23
n = 12
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
obstacleGrid = [[0,0],[1,1],[0,0]]
obstacleGrid = [[1,0]]

sol = Solution()
print(sol.uniquePaths(m, n))
print(sol.uniquePathsWithObstacles(obstacleGrid))
