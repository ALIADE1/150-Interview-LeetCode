class Solution:
    def rob(self, nums: List[int]) -> int:
        a1,a2 = 0,0

        for x in nums:
            val = max(x+a2,a1)
            a1,a2 = val,a1
            
        return a1
      
