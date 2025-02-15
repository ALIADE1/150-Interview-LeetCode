# Problem: https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ""
        for x in s:
            if x.isalnum():
                ss+=x.lower()

        return  ss == ss[::-1]
