from typing import List


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

grid = [
    ["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],
    ["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],
    ["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],
    ["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],
    ["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],
    ["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],
    ["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
    ["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],
    ["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],
    ["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],
    ["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],
    ["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],
    ["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],
    ["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],
    ["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],
    ["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],
    ["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],
    ["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],
    ["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],
    ["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]] # 58

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         count = 0
#         queue = []
#         visited = []
#         H, W = len(grid), len(grid[0])
#         for y in range(H):
#             temp = []
#             for x in range(W):
#                 temp.append(0)
#             visited.append(temp)

#         for y in range(H):
#             for x in range(W):
#                 if grid[y][x] == "1" and visited[y][x] == 0:
#                     count += 1
#                     queue = [(y, x)]
#                     while len(queue) > 0:
#                         position = queue[0]
#                         visited[y][x] = 1
#                         queue = self.bfs(grid, position, queue, visited)
#                         queue = queue[1:]
#         return count

#     def bfs(self, grid, position, queue, visited):
#         y, x = position
#         H, W = len(visited), len(visited[0])
#         neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]
#         for (dy, dx) in neighbors:
#             vx, vy = x + dx, y + dy
#             if 0 <= vx and vx < W and 0 <= vy and vy < H and grid[vy][vx] == "1" and visited[vy][vx] == 0:
#                 visited[vy][vx] = 1
#                 queue.append((vy, vx))
#         return queue


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = []
        H, W = len(grid), len(grid[0])
        for y in range(H):
            temp = []
            for x in range(W):
                temp.append(0)
            visited.append(temp)

        for y in range(H):
            for x in range(W):
                if self.explore(grid, y, x, visited):
                    count += 1

        return count

    def explore(self, grid, y, x, visited):
        H, W = len(grid), len(grid[0])
        row_bound = 0 <= x and x < W
        col_bound = 0 <= y and y < H
        if not row_bound or not col_bound: return False
        if grid[y][x] == "0": return False
        if visited[y][x] == 1: return False

        visited[y][x] = 1
        self.explore(grid, y - 1, x, visited)
        self.explore(grid, y + 1, x, visited)
        self.explore(grid, y, x - 1, visited)
        self.explore(grid, y, x + 1, visited)
        return True

sol = Solution()
cost = sol.numIslands(grid)
print(cost)
