class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        summ = 0

        for x in range(n):
            if n % (x+1) == 0:
                summ+= (nums[x]*nums[x])

        return summ
