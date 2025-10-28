class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0

        for x, y in enumerate(s):
            ans+=abs(x - t.find(y))

        return ans
