class Solution:
    def isHappy(self, n: int) -> bool:
        ans = n

        for _ in range(100):

            summ = 0
            for x in str(ans):
                summ += pow(int(x),2)

            ans = summ
            if ans == 1:
                return True

        return False
      
