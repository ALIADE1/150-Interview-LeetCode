class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True
        else:
            for x in range(1,n):
                if (nums[x] % 2 == 0 and nums[x-1] % 2 == 1) or nums[x] % 2 == 1 and nums[x-1] % 2 == 0:
                    continue
                else:
                    return False

        return True
