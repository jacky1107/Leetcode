#include <string>
#include <stdio.h>
#include <iostream>
using namespace std;

class Solution {
public:
    int maxScore(string s) {
        int max_len = 0;
        for (size_t i = 1; i < s.size(); i++)
        {
            int m = calculate(s, 0, i) + calculate(s, i, s.size());
            if (m > max_len) max_len = m;
        }
        return max_len;
    }

    int calculate(string s, int start, int end) {
        int res = 0;
        for (size_t i = start; i < end; i++)
        {
            int r = s[i] - '0';
            if (!start)  res += (r ^ 1);
            else res += r;
        }
        return res;
    }
};

int main() {
    string s = "011101";
    Solution sol;
    int result = sol.maxScore(s);
    printf("%d\n", result);
    return 0;
}