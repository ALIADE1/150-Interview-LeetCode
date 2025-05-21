class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []
        n = len(nums2)
        for x in nums1:
            b = True
            i = nums2.index(x)
            val = x
            for j in range(i+1,n):
                if nums2[j] > val:
                    ans.append(nums2[j])
                    b = False
                    break
            if b:
                ans.append(-1)
        return ans
