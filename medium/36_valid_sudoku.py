from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        H, W = len(board), len(board[0])
        for y in range(H):
            temp = {}
            for x in range(W):
                if board[y][x] == ".": continue
                elif board[y][x] not in temp: temp[board[y][x]] = True
                else: return False

        for x in range(W):
            temp = {}
            for y in range(H):
                if board[y][x] == ".": continue
                elif board[y][x] not in temp: temp[board[y][x]] = True
                else: return False

        for y in range(0, H, 3):
            for x in range(0, W, 3):
                temp = {}
                for i in range(y, y + 3):
                    for j in range(x, x + 3):
                        if board[i][j] == ".": continue
                        elif board[i][j] not in temp: temp[board[i][j]] = True
                        else: return False

        return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board =[
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

sol = Solution()
res = sol.isValidSudoku(board)
print(res)
