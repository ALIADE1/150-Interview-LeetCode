class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]
        c = b.count('1')
        return c
      
