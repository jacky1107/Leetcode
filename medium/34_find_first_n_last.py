from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start = self.binary_search(nums, target)
        end = self.binary_search(nums, target + 1)
        return [-1, -1] if start >= end or start == len(nums) else [start, end - 1]
    
    def binary_search(self, nums, target):
        a = 0
        b = len(nums)
        while a < b:
            index = (a + b) // 2
            if target <= nums[index]:
                b = index
            else:
                a = index + 1
        return a

nums = [5,7,8,8,9,9, 9, 9,9,9,10,10,10]
nums = [5,7,7, 7,7,7, 7,7,7, 7,8,8,10]
nums = [5,8,8, 8,8,8, 8,8,8, 8,8,8,10]
nums = [2, 2]
nums = [5,8,8,8,10]
nums = [5,7,7,8,8,10]
target = 6
sol = Solution()
output = sol.searchRange(nums, target)
print(output)
