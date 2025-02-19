class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        vector<int> ve;
        ve.reserve(n + m);
        
        ve.insert(ve.end(), nums1.begin(), nums1.end());
        ve.insert(ve.end(), nums2.begin(), nums2.end());
        
        sort(ve.begin(), ve.end());
        int t = n + m;
        
        if (t % 2 != 0) 
            return static_cast<double>(ve[t / 2]);
        else 
            return (static_cast<double>(ve[t / 2]) + static_cast<double>(ve[t / 2 - 1])) / 2.0;
        
    }
};
