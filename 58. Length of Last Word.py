'''
Time Complexity: O(n)

Space Complexity: O(n)

Problem: https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        last_space_index = s.rfind(' ')
        return len(s) - last_space_index - 1

  
