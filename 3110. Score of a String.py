class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for x in range(len(s)-1):
            ans+=abs(ord(s[x]) - ord(s[x+1]))

        return ans
