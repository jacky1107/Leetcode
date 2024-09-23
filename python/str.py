
from typing import List

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i, j = 0, len(s) - 1

        s = list(s)
        while i < j:
            if (s[i] == "-"):
                i += 1
            
            elif (s[j] == "-"):
                j -= 1
            
            elif not s[i].isalpha():
                i += 1
                
            elif not s[j].isalpha():
                j -= 1
            
            else:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i += 1
                j -= 1

        return "".join(s)

s = "a-bC-dEf-ghIj"
s = "Test1ng-Leet=code-Q!"
sol = Solution()
print(sol.reverseOnlyLetters(s))