class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fre = [0] * n
        ans = []

        for x in nums:
            fre[x]+=1

        for x in range(0,n):
            if fre[x] > 1:
                ans.append(x)

        return ans
