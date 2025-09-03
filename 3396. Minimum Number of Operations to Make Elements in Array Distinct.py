class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for x in range(0,n,3):
            if len(nums[x:]) == len(set(nums[x:])):
                return ans
            else:
                ans+=1  

        return ans
