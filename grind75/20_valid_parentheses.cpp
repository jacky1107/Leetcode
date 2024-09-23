#include <stdio.h>
#include <iostream>

#include <map>
#include <stack>
#include <vector>
#include <string.h>
#include <unordered_map>

class Solution {
public:
    bool isValid(std::string s) {
        std::map<char, char> table {
            {')', '('},
            {'}', '{'},
            {']', '['},
        };
        std::stack<char> st;
        for (char c : s) {
            if (!table.count(c)) st.push(c);
            else if (st.empty() || st.top() != table[c]) return false;
            else st.pop();
        }
        return st.empty();
    }
};

int main() {
    std::string s = "()";
    Solution sol;
    bool res = sol.isValid(s);
    std::cout << res << std::endl;
    return 0;
}