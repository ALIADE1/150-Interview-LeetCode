class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(range(0,n+1))
        summ = sum(nums)

        return total_sum - summ
