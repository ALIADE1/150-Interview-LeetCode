class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        minn = min(a,b)

        for x in range(1,minn+1):
            if a % x == 0 and b % x == 0:
                ans+=1

        return ans
