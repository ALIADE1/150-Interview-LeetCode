class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        all_summ = sum(nums)
        dig_summ = 0

        for x in nums:
            s = str(x)
            for i in s:
                dig_summ+=int(i)

        return abs(all_summ - dig_summ)
