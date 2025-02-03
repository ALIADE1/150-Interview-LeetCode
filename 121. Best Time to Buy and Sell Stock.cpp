/*

=> Time Complexity: O(n)
=> Space Complexity: O(1)

problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
*/


#include <vector>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() < 2) return 0; 

        int minPrice = prices[0];
        int maxProfit = 0;

        for (int x = 1; x < prices.size(); x++) {
            if (prices[x] < minPrice) {
                minPrice = prices[x]; 
            } else {
                maxProfit = max(maxProfit, prices[x] - minPrice); 
            }
        }

        return maxProfit;
    }
};
