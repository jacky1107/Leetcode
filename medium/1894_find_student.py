from itertools import accumulate
from tabnanny import check
from typing import List


class Solution:
    # fast
    def chalkReplacerBinary(self, chalk: List[int], k: int) -> int:
        if len(chalk) == 0:
            return None
        chalk = list(accumulate(chalk))
        k = k % chalk[-1]
        left, right = 0, len(chalk)
        while left < right:
            mid = (left + right) >> 1
            if chalk[mid] > k:
                right = mid
            else:
                left = mid + 1
        return left

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        if len(chalk) == 0:
            return None
        
        k = k % sum(chalk)
        idx = 0
        while k >= 0:
            k -= chalk[idx]
            if k < 0:
                break
            idx += 1
            if idx >= len(chalk): idx = 0

        return idx

k = 22
chalk = [5,1,5]
sol = Solution()
idx = sol.chalkReplacerBinary(chalk, k)
print(idx)