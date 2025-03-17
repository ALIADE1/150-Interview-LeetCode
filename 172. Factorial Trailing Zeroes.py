class Solution:
    def trailingZeroes(self, n: int) -> int:
        s = 0
        d = 5
        while n >= d:
            s += (n//d)
            d *= 5
        return s
      
