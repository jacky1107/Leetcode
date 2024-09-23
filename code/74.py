from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        H, W = len(matrix), len(matrix[0])
        l, r = 0, (H * W)
        while l < r:
            m = (l + r) // 2
            i, j = m // W, m % W
            if target < matrix[i][j]:
                r = m
            elif target > matrix[i][j]:
                l = m + 1
            else:
                return True
        return False

matrix = [[1]]
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
sol = Solution()
print(sol.searchMatrix(matrix, 13))