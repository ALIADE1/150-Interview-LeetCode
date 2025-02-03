"""
=> Time Complexity: O(n)
=> Space Complexity: O(1)

problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution(object):
    def removeDuplicates(self, nums):
        i = 2
        for x in range(2,len(nums)):
            if nums[x]!=nums[i-2]:
                nums[i]=nums[x]
                i+=1

        return i
      
