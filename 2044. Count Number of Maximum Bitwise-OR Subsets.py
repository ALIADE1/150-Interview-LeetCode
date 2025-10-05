class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxxor = 0
        for x in nums:
            maxxor |= x

        def func(i, summ):
            if i == len(nums):
                if summ == maxxor:
                    return 1
                else:
                    return 0
            inn = func(i+1, summ | nums[i])
            exx = func(i+1, summ)
            return inn + exx

        return func(0,0)
