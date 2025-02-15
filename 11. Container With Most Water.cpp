/*
Time Complexity: O(n)

Space Complexity: O(1)

Problem: https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
*/

class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        long long maxx = 0; 
        while (r > l) {
            maxx = max(maxx, valu(height, l, r));
            if (height[l] < height[r])
                l++;
            else
                r--; 
        }
        return maxx;  
    }

private:
    long long valu(vector<int>& height, int l, int r) {
        return min(height[l], height[r]) * (r - l); 
    }
};

