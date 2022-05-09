"""
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        best = sum(nums[:3])
        for i in range(len(nums) - 2):  # 最多到長度-2，因為他是最小值，所以要保留
            s = i + 1
            e = len(nums) - 1
            while s < e:
                new = nums[i] + nums[s] + nums[e]
                # 判斷新進來的值，距離是不是比較小，小的話就儲存結果
                if abs(target - new) < abs(target - best):
                    best = new
                if new < target:  # 每一次都判斷新的值，究竟是比較大還是小，若比較小，就往大的方向走，反之
                    s += 1
                else:
                    e -= 1
        return best


nums = [1, 2, 4, 8, 16, 32, 64, 128]
target = 82
sol = Solution()
res = sol.threeSumClosest(nums, target)
print(res)