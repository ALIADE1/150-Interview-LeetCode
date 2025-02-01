"""
Time Complexity: O(n)

Space Complexity: O(1)

Problem: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
"""


class Solution(object):
    def removeElement(self, nums, val):
        r = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[r] = nums[x]
                r+=1
        return r
