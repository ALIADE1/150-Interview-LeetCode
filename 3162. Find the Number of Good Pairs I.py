class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        n, m = len(nums1), len(nums2)

        for i in range(0,n):
            for j in range(0,m):
                if nums1[i] % (nums2[j] * k) == 0:
                    ans+=1

        return ans
