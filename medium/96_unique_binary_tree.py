class Solution:
    def numTrees(self, n: int) -> int:
        memory = [0] * (n + 1)
        memory[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                memory[i] += memory[j] * memory[i-j-1]
        return memory[-1]

n = 3
sol = Solution()
res = sol.numTrees(n)
print(res)
