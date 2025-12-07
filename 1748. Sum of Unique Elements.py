class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cou = [0] * 102
        ans = 0
        for x in nums:
            cou[x]+=1

        for v in nums:
            if cou[v] == 1:
                ans+=v
            else:
                continue

        return ans
