class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cou1, cou2 = 0, 0

        for x in nums1:
            if x in nums2 :
                cou1+=1

        for x in nums2:
            if x in nums1:
                cou2+=1

        return [cou1,cou2]
