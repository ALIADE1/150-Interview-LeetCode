class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1,num2 = 0,0

        for x in range(1,n+1):
            if x%m!=0:
                num1+=x

        for x in range(1,n+1):
            if x%m==0:
                num2+=x
            
        return num1-num2
