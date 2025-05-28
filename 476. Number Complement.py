class Solution:
    def findComplement(self, num: int) -> int:
        l = len(bin(num)[2:])
        i = 2**(l)-1
        return num ^ i
      
