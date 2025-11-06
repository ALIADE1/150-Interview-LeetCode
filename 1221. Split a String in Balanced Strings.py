class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        l, r = 0, 0

        for x in s:
            if x == 'R':
                r+=1
            elif x == 'L':
                l+=1

            if l == r:
                ans+=1
                l, r = 0, 0
        
        return ans
