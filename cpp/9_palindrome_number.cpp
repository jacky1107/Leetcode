#include <stdio.h>
#include <string.h>
#include <vector>
#include <unordered_map>

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        int backup = x;
        long int reverse = 0;

        while (x)
        {
            reverse = reverse * 10 + x % 10;
            x /= 10;
        }
        return reverse == backup;
    }
};

int main() {
    int x = 121;
    int results;
    Solution sol;
    results = sol.isPalindrome(x);
    printf("%d\n", results);
    return 0;
}