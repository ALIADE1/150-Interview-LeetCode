class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();        
        int minLen = n + 1; 
        int left = 0;
        long long windowSum = 0;
        
        for (int right = 0; right < n; right++) {
            windowSum += nums[right];
            
            while (windowSum >= target) {
                minLen = min(minLen, right - left + 1);
                windowSum -= nums[left];
                left++;
            }
        }
        return minLen == n + 1 ? 0 : minLen;
    }
};
