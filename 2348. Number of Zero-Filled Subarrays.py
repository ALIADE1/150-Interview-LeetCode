class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        li = []

        for x in nums:
            if x == 0:
                li.append(1)
            else:
                li.append(0)

        for i in range(1,len(nums)):
            if  li[i] == 1:
                li[i]+=li[i-1]

        ans = sum(li)
        return ans
