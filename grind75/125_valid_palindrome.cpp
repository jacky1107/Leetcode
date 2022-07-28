#include <iostream>
#include <vector>
#include <string.h>
#include <ctype.h>
#include <cctype>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size();
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        while (l < r)
        {
            if (!isalnum(s[l])) l++;
            else if (!isalnum(s[r])) r--;
            else if (s[l] != s[r]) return false;
            else {
                r--;
                l++;
            }
        }
        return true;
    }
};

int main(void) {
    string s = "A man, a plan, a canal: Paxama";
    Solution sol;
    bool res = sol.isPalindrome(s);
    cout << res << endl;
}
