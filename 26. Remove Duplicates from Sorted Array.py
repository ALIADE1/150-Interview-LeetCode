"""
=> Time Complexity: O(n)
=> Space Complexity: O(1)

problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        for x in range(0,len(nums)-1):
            if nums[x]!=nums[x+1] :
                nums[i]=nums[x+1]
                i+=1

        return i
      
