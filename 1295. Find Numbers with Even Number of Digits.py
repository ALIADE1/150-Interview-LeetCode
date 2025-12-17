class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cou_ans = 0

        for x in nums:
            if len(str(x)) % 2 == 0:
                cou_ans+=1

        return cou_ans
