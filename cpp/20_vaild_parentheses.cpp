#include <stdio.h>
#include <string>
#include <stack>
#include <map>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        map<char, char> table {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        stack<char> st;

        for (size_t i = 0; i < s.size(); i++)
        {
            if (!table.count(s[i])) st.push(s[i]);
            else if (st.empty() || st.top() != table[s[i]]) return false;
            else st.pop();
        }
        return st.empty();
    }
};

int main() {
    string s = "(){})";
    Solution sol;
    int result = sol.isValid(s);
    printf("%d\n", result);
    return 0;
}