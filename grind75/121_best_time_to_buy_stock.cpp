#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int buy = 100000;
        for(int price : prices) {
            buy = min(price, buy);
            if (price - buy >= res) {
                res = price - buy;
            }
        }
        return res;
    }
};

int main(void) {
    vector<int> prices = {7,1,8,3,7,4};
    Solution sol;
    int res = sol.maxProfit(prices);
    cout << res << endl;
}
