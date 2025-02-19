class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        return find(nums, target);
    }

private:
    vector<int> find(vector<int>& nums, int target) {
        int r = 0, l = nums.size() - 1;
        int x = -1;

        while (r <= l) {
            int mid = r + (l - r) / 2;
            if (nums[mid] == target) {
                x = mid;
                break;
            } else if (nums[mid] < target) 
                r = mid + 1;
              else 
                l = mid - 1;
        }

        if (x == -1) 
            return {-1, -1};

        int s = x, e = x;

        while (s > 0 && nums[s - 1] == target) 
            s--;

        while (e < nums.size() - 1 && nums[e + 1] == target) 
            e++;
          
        return {s, e};
    }
};
