class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ, prod = 0, 1

        for x in str(n):
            summ += int(x)
            prod *= int(x)

        return prod - summ
