class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        fre = Counter(nums)
        for v,c in fre.items():
            if c == 1:
                return v
              
