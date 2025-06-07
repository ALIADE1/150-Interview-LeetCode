class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []

        for x in range(left,right+1):
            if x < 10:
                ans.append(x)
            else:
                b = True
                for i in str(x):
                    if int(i) == 0 or x%int(i) != 0:
                        b = False
                if b:
                    ans.append(x)

        return ans
