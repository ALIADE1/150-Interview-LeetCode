class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = []
        for x in nums:
            s = str(x)
            summ = 0
            for i in range(len(s)):
                summ+=int(s[i])
            ans.append(summ)

        return min(ans)
