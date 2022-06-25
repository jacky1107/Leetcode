#include <stdio.h>
#include <string.h>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::unordered_map<char, int> table = {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50},
        {'C', 100},
        {'D', 500},
        {'M', 1000}
    };

    int romanToInt(std::string s) {
        int result = 0;
        for (size_t i = s.size(); i-- > 0;)
        {
            int now = table[s[i]];
            if (i != 0 && table[s[i - 1]] < now)
            {
                result += (now - table[s[i - 1]]);
                i--;
            } else {
                result += now;
            }
        }
        return result;
    }
};


int main() {
    std::string s = "LVIII";
    Solution sol;
    int result = sol.romanToInt(s);
    printf("%d\n", result);
    return 0;
}