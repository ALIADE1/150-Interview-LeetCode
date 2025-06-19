class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for z in range(2**n):
            xor = 0
            for x in range(n):
                if z & (2**x):
                    xor ^= nums[x]
            ans += xor
            
        return ans
