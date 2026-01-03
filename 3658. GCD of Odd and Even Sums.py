class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd, sumEven = 0, 0
        rang = 2*n + 1

        for x in range(1,rang):
            if x % 2 == 0:
                sumEven+=x
            else:
                sumOdd+=x

        return gcd(sumEven,sumOdd)
