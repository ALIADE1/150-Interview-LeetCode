class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        ans+=1
        
        return ans
