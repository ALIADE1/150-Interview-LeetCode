class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for x in range(2,n-1):
            s = bin(x)[2:]
            if s != s[::-1]:
                return False
            else:
                continue
                
        return True
