
/*

Time Complexity: O(n)

Space Complexity: O(1)

Problem: https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

*/


class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> ma = {
            {'I', 1}, {'V', 5}, {'X', 10}, {'L', 50}, 
            {'C', 100}, {'D', 500}, {'M', 1000}
        }; 
        int cou = 0;
        int n = s.size();
        
        for (int x = 0; x < n; ++x) {
            if (x > 0 && ma[s[x]] > ma[s[x-1]]) 
                cou += ma[s[x]] - 2 * ma[s[x-1]];
            else 
                cou += ma[s[x]];
        }
        return cou;
    }
};
