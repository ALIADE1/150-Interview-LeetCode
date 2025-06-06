class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)

        for x in range(n):
            if nums[x] != 0:
                nums[i] = nums[x]
                i+=1

        while n > i:
            nums[i] = 0
            i+=1
        
