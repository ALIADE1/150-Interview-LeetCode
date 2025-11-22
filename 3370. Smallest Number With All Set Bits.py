class Solution:
    def smallestNumber(self, n: int) -> int:
        for x in range(n,1000000):
            bi = bin(x)[2:]

            if bi.count('1') == len(bi):
                return x
