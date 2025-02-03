/*

=> Time Complexity: O(n)
=> Space Complexity: O(n)

problem: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
*/



class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> ma;
        for (auto x : nums)
            ma[x]++;

        int m = 0;
        int r = 0;
        for (const auto& x : ma) {
            if (x.second > m) {
                m = x.second;
                r = x.first;
            }
        }
        return r;
    }
};
