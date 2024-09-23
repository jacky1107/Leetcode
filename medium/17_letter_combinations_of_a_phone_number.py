from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        length = len(digits)
        if length == 0: return res
        def back_tracking(current_length, string):
            if length == current_length: res.append(string)
            else:
                for letter in table[digits[current_length]]:
                    back_tracking(current_length + 1, string+letter)

        back_tracking(0, "")
        return res


digits = "23"
sol = Solution()
res = sol.letterCombinations(digits)
print(res)
