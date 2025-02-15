
/*
Time Complexity: O(n)

Space Complexity: O(1)

problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size()-1;
        while(true){
            if(numbers[l]+numbers[r]==target)
                return {l + 1, r + 1};
            else if(numbers[l]+numbers[r]>target)
                r--;
            else
                l++;
        }
    }
};
