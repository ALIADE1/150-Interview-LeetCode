class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, n-1
            while r>l:
                summ = nums[l] + nums[r] + nums[i]
                if summ >0:
                    r-=1
                elif summ <0:
                    l+=1
                else:
                    ans.append([nums[l] , nums[r] , nums[i]])
                    while r>l and nums[r] == nums[r-1]:
                        r-=1
                    while r>l and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
        return ans
      
