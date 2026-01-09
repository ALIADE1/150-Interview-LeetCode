class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        ans = []

        for i in range(n):
            freq, val = nums[2*i], nums[2*i+1]
            for x in range(freq):
                ans.append(val)

        return ans
