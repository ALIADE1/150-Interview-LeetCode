class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int,int> ans;
        int n = nums.size();
        for(int x=0;x<n;x++){
            if(ans.find(nums[x])!=ans.end()){
                if(abs(x-ans[nums[x]])<=k)
                    return true;
            }
            ans[nums[x]] = x;
        }
        return false;   
    }
};
