from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 0

        def check(string):
            if string[0] == "0": return 0
            n = int(string)
            if 0 <= n and n <= 26:
                return 1
            return 0

        res = 1
        for i in range(len(s) - 1, -1, -1):
            if (i - 1) >= 0:
                res += check(s[i-1:i+1])
        
        return res



s = "226"
s = "06"
sol = Solution()
print(sol.numDecodings(s))