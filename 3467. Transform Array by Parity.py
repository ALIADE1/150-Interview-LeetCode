class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        i = 0

        for x in nums:
            if x % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
            i+=1
            
        nums.sort()
        return nums
