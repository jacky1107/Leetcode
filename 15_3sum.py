from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            diff = target - num
            if num in hash_table:
                hash_table[num].append(i)
                return hash_table[num]
            else:
                hash_table[diff] = [i]
        return []

nums = [2, 7, 8, 11]
sol = Solution()
result = sol.twoSum(nums, 9)
print(result)
