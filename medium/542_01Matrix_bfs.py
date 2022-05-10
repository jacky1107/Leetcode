"""
BFS also known as Breadth-First Search
"""
from typing import List
import copy

mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
mat = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
    [0, 0, 0],
]
# mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        H = len(mat)
        W = len(mat[0])
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        queue = []
        result = []
        visited = []
        for y in range(H):
            temp = []
            res_temp = []
            for x in range(W):
                res_temp.append(0)
                if mat[y][x] == 0:
                    queue.append((y, x))
                    temp.append(1)
                else:
                    temp.append(0)
            visited.append(temp)
            result.append(res_temp)

        cost = 0
        while len(queue) != 0:
            new_queue = []
            for i in range(len(queue)):
                (y, x) = queue[i]

                if mat[y][x] == 1:
                    result[y][x] = cost

                for (dy, dx) in dirs:
                    dy = y + dy
                    dx = x + dx
                    if (
                        0 <= dy
                        and dy < H
                        and 0 <= dx
                        and dx < W
                        and not visited[dy][dx]
                    ):
                        new_queue.append((dy, dx))
                        visited[dy][dx] = 1
            queue = new_queue
            cost += 1

        return result

    def bfs(self, queue, mat, visited, H, W):
        new_q = []
        for (y, x) in queue:
            visited.append([y, x])
            if (y - 1) >= 0 and [y - 1, x] not in visited:
                new_q.append([y - 1, x])
            if (x - 1) >= 0 and [y, x - 1] not in visited:
                new_q.append([y, x- 1])
            if (y + 1) < H and [y + 1, x] not in visited:
                new_q.append([y + 1, x])
            if (x + 1) < W and [y, x + 1] not in visited:
                new_q.append([y, x + 1])
        return new_q

sol = Solution()
mat = sol.updateMatrix(mat)
print(mat)
