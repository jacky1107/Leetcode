#include <stdio.h>
#include <string.h>
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> results;
        std::unordered_map<int, int> hash_table;

        for (size_t i = 0; i < nums.size(); i++)
        {
            int num = nums[i];
            if(hash_table.find(num) == hash_table.end()) {
                hash_table[target - num] = i;
            } else {
                results.push_back(hash_table[num]);
                results.push_back(i);
            }
        }
        return results;
    }
};

void print_array(std::vector<int> &array) {
    for (size_t i = 0; i < array.size(); i++)
    {
        printf("%d ", array[i]);
    }
}

int main() {
    std::vector<int> results;
    std::vector<int> nums = {3,3};
    int target = 6;
    Solution sol;
    results = sol.twoSum(nums, target);
    print_array(results);
    return 0;
}