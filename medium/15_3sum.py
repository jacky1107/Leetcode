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

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i, num in enumerate(nums[:-2]):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = num + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    if [num, nums[l], nums[r]] not in results:
                        results.append([num, nums[l], nums[r]])
                    l += 1
        return results

nums = [2, 7, 8, 11]
sol = Solution()
result = sol.twoSum(nums, 9)
# print(result)

nums = [0,0,0,0,0]
nums = [-1,0,1,2,-1,-4]
nums = [-2, 0, 1, 1, 2]
result = sol.threeSum(nums)
print(result)