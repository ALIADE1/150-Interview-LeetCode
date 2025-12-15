class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cou_ans = 0

        for x in nums:
            if x < k:
                cou_ans+=1

        return cou_ans
