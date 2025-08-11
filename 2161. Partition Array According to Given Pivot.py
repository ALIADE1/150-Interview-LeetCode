class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []

        for x in nums:
            if x < pivot:
                ans.append(x)

        for x in nums:
            if x == pivot:
                ans.append(x)

        for x in nums:
            if x > pivot:
                ans.append(x)
            
        return ans
