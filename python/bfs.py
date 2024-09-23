from typing import List
import collections

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(board, visited, y, x, H, W, queue):
            if y < 0 or y >= H: return
            if x < 0 or x >= W: return
            if (y, x) in visited: return
            visited.append((y, x))
            if board[y][x] == "O":
                queue.append((y, x))
                board[y][x] = "G"
                bfs(board, visited, y - 1, x, H, W, queue)
                bfs(board, visited, y, x - 1, H, W, queue)
                bfs(board, visited, y + 1, x, H, W, queue)
                bfs(board, visited, y, x + 1, H, W, queue)

        visited = []
        H, W = len(board), len(board[0])
        for y in range(H):
            for x in range(W):
                queue = []
                if y == 0 or x == 0 or y == (H - 1) or x == (W - 1):
                    queue.append((y, x))
                    while len(queue) > 0:
                        (py, px) = queue[0]
                        queue = queue[1:]
                        bfs(board, visited, py, px, H, W, queue)

        for y in range(H):
            for x in range(W):
                if board[y][x]=='O':
                    board[y][x]='X'
                elif board[y][x]=='G':
                    board[y][x]='O'



board = [
    ["X","O","O","X","X","X","O","X","O","O"],
    ["X","O","X","X","X","X","X","X","X","X"],
    ["X","X","X","X","O","X","X","X","X","X"],
    ["X","O","X","X","X","O","X","X","X","O"],
    ["O","X","X","X","O","X","O","X","O","X"],
    ["X","X","O","X","X","O","O","X","X","X"],
    ["O","X","X","O","O","X","O","X","X","O"],
    ["O","X","X","X","X","X","O","X","X","X"],
    ["X","O","O","X","X","O","X","X","O","O"],
    ["X","X","X","O","O","X","O","X","X","O"]]
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

sol = Solution()
print(sol.solve(board))
