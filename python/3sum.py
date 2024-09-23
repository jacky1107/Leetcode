
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            first, last = matrix[i][0], matrix[i][-1]
            if first <= target and target <= last:
                s = 0
                e = len(matrix[i])
                while (s + 1) < e:
                    middle = (s + e) // 2
                    print(s, middle, e)
                    if target < matrix[i][middle]:
                        e = middle
                    elif target > matrix[i][middle]:
                        s = middle
                    else:
                        return True
                    print(s, middle, e)

        return False


sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1, 3]]
print(sol.searchMatrix(matrix, 1))