class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(1, n + 1):
            ans.append(sum(nums[0:i]))

        return ans
