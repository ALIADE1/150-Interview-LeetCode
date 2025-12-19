class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        ans_max = 0

        for x in s:
            if x == 'L':
                ans-=1
            else:
                ans+=1
            ans_max = max(ans_max,ans)

        return ans_max
