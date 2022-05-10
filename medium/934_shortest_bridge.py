from typing import List
import copy

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = []
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = copy.deepcopy(grid)

        H, W = len(grid), len(grid[0])
        for y in range(H):
            for x in range(W):
                if grid[y][x]:
                    queue.append((y, x))

        while len(queue) != 0:
            new_q = []
            for (y, x) in queue:
                for dir in dirs:
                    dy = y + dir[0]
                    dx = x + dir[1]
                    if (0 <= dy and dy < H and 0 <= dx and dx < W and visited[dy][dx] != 1):
                        new_q.append((dy, dx))
                        visited[dy][dx] = 1
            queue = new_q
            print(queue)

grid = [[0,1,0],[0,0,0],[0,0,1]]
sol = Solution()
sol.shortestBridge(grid)