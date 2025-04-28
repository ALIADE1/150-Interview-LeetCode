class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1] * n

        for x in range(1,n):
            if ratings[x] > ratings[x-1]:
                ans[x] = ans[x-1] + 1
        
        for x in range(n-2,-1,-1):
            if ratings[x] > ratings[x+1]:
                ans[x] = max(ans[x+1] + 1,ans[x])
                
        return sum(ans)
      
