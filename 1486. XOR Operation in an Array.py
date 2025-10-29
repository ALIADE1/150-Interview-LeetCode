class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = []
        ans = 0

        for x in range(n):
            arr.append(start + 2*x)

        for x in arr:
            ans^=x

        return ans
