#include <stdio.h>
#include <iostream>

#include <map>
#include <stack>
#include <vector>
#include <string.h>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> res;
        std::unordered_map<int, int> table;

        for (size_t i = 0; i < nums.size(); i++)
        {
            if (table.find(nums[i]) != table.end()) {
                res.push_back(table[nums[i]]);
                res.push_back(i);
            } else {
                table[target - nums[i]] = i;
            }
        }
        
        return res;
    }
};
int main() {
    std::vector<int> res;
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    Solution sol;
    res = sol.twoSum(nums, target);
    for (size_t i = 0; i < res.size(); i++)
    {
        std::cout << res[i] << std::endl;
    }
    return 0;
}