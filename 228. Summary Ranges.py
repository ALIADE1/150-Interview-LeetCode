class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        lenn = len(nums)
        ans =[]
        start = nums[0]
    
        for x in range(1,lenn):
            if nums[x] == nums[x-1] + 1:
                continue
            else:
                if start == nums[x - 1]:
                    ans.append(f"{start}")
                else:
                    ans.append(f"{start}->{nums[x - 1]}")
                start = nums[x]
        
        if start == nums[-1]:
            ans.append(f"{nums[-1]}")
        else:
            ans.append(f"{start}->{nums[-1]}")

        return ans
