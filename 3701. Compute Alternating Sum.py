class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for x in range(n):
            if x % 2 == 0:
                ans += (nums[x])
            else:
                ans += (nums[x] * -1)

        return ans
