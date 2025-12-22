class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans_cou = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j]) == k:
                    ans_cou+=1

        return ans_cou
