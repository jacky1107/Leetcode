from itertools import accumulate
from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        delta = [0] * length
        for start, end, inc in updates:
            delta[start] += inc
            if end + 1 < length:
                delta[end + 1] -= inc
        print(delta)
        return list(accumulate(delta))


l = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
sol = Solution()
print(sol.getModifiedArray(l, updates))