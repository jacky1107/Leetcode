from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        H, W = len(matrix), len(matrix[0])
        self.matrix = [[0] * (W+1) for _ in range(H+1)]
        for r in range(H):
            for c in range(W):
                self.matrix[r+1][c+1] = matrix[r][c] + self.matrix[r+1][c] + self.matrix[r][c+1] - self.matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1] - self.matrix[row2+1][col1] - self.matrix[row1][col2+1] + self.matrix[row1][col1] 

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2,1,4,3))
print(numMatrix.sumRegion(1,1,2,2))
print(numMatrix.sumRegion(1,2,2,4))