
class Solution:
    def countPairs(self, nums, k: int) -> int:
        pairs = 0
        table = {}
        for i in range(len(nums)):
            if nums[i] not in table:
                table[nums[i]] = [i]
            else:
                for j in range(len(table[nums[i]])):
                    if (table[nums[i]][j] * i) % 2 == 0:
                        pairs += 1
                table[nums[i]].append(i)

        return pairs

    
k = 2
nums = [3,1,2,2,2,1,3]
sol = Solution()
sol.countPairs(nums, k)


a = 5
b = 4
c = 3

r = max(a, c)
s = min(a, c)
p = min(a, c)

p = min(a, b, c)
q = max(min(a, c), b)

p = min(a, b, c)
q = max(min(a, c), b)
r = max(a, c)
print(p, q, r)

