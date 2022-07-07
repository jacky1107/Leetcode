#include <stdio.h>
#include <string.h>
#include <vector>
#include <unordered_map>
using namespace std;



class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";
        if (strs.size() == 1) return strs[0];
        
        string res = "";
        int min_len = 10000;
        for (size_t i = 0; i < strs.size(); i++)
        {
            int len = strs[i].size();
            if (len < min_len) min_len = len;
        }

        for (size_t i = 0; i < min_len; i++)
        {
            for (size_t j = 0; j < strs.size() - 1; j++)
            {
                if (strs[j][i] != strs[j+1][i]) return res;
            }
            res += strs[0][i];
        }
        return res;
    }
};


int main() {
    vector<string> strs = {"flower","flow","flight"};
    Solution sol;
    string result = sol.longestCommonPrefix(strs);
    printf("%s\n", result.c_str());
    return 0;
}