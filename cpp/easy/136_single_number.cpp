#include <stdio.h>
#include <iostream>

#include <vector>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int target = 0;
        for (size_t i = 0; i < nums.size(); i++)
        {
            target ^= nums[i];
        }
        return target;
    }
};

int main() {
    vector<int> nums = {4, 1, 2, 2, 1};
    Solution sol;
    int result = sol.singleNumber(nums);
    printf("%d\n", result);
    return 0;
}