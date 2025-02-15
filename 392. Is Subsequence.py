# Problem: https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        n,m = len(s),len(t)

        while j < m and i < n:
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == n
