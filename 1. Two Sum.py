class Solution(object):
    def twoSum(self, nums, target):
        pos = {}
        for i, n in enumerate(nums):
            e = target - n
            if e in pos:
                return [pos[e], i]
            pos[n] = i
          
