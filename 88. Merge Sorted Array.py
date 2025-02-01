"""
Time Complexity: O(m + n)

Space Complexity: O(1)
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        q, w, e = m-1, n-1, m+n-1

        while q >= 0 and w >= 0:
            if nums1[q] > nums2[w]:
                nums1[e] = nums1[q]
                q -= 1
            else:
                nums1[e] = nums2[w]
                w -= 1
            e -= 1

        # If there are remaining elements in nums2, copy them
        while w >= 0:
            nums1[e] = nums2[w]
            w -= 1
            e -= 1

        return nums1
