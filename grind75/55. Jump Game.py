from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i]
            if (i + jump) >= goal:
                goal = i
        
        return goal == 0

nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
sol = Solution()
res = sol.canJump(nums)
print(res)
