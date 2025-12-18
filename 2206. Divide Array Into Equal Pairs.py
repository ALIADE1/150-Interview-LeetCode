class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = [0] * 501

        for x in nums:
            freq[x]+=1

        for x in freq:
            if x % 2 == 1:
                return False

        return True
