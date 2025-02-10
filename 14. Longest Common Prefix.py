'''
Time Complexity: O(m*n)

Space Complexity: O(m)

Problem: https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150

'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        ss = strs[0]
        re = ""
        for i in range(len(ss)):
            for s in strs:
                if(i==len(s) or ss[i]!=s[i]):
                    return re;
            re += ss[i];
        return re;
      
