class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n % 2 == 0:
            ans = []
            c = n // 2
            for x in range(1,c+1):
                ans.append(x)
            for x in range(1,c+1):
                ans.append(-x)
            return ans
        else:
            ans = [0]
            c = n // 2
            for x in range(1,c+1):
                ans.append(x)
            for x in range(1,c+1):
                ans.append(-1*x)
            return ans
