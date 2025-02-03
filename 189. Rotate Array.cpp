/*

=> Time Complexity: O(n)
=> Space Complexity: O(n)

problem: https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
*/



class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n; // Handle cases where k is larger than n
        vector<int> arr(n);
        int p = 0;

        for (int x = n - k; x < n; x++) {
            arr[p] = nums[x];
            p++;
        }
      
        for (int x = 0; x < n - k; x++) {
            arr[p] = nums[x];
            p++;
        }
      
        for (int x = 0; x < n; x++) {
            nums[x] = arr[x];
        }
    }
};

