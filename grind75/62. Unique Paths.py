class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[1] * m for _ in range(n)] 

        for y in range(1, m):
            for x in range(1, n):
                memo[y][x] = memo[y-1][x] + memo[y][x-1]
        
        return memo[m-1][n-1]
