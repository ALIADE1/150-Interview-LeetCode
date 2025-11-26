class Solution:
    def countAsterisks(self, s: str) -> int:
        s_list = s.split('|')
        n = len(s_list)
        ans = 0

        for x in range(0,n,2):
            ans+= s_list[x].count('*')

        return ans
