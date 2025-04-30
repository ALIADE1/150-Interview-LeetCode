class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [1] * n

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans[i] = max(ans[i],ans[j]+1)
        return max(ans)
      
