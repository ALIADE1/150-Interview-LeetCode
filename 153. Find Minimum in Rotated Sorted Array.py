class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1

        if n == 1:
            return nums[0]
        elif nums[l] <= nums[r]:
            return nums[l]
        else:
            while l<=r:
                mid = (r+l) // 2
                if  mid < n-1 and nums[mid + 1] < nums[mid]:
                    return nums[mid+1]
                elif mid > 0 and nums[mid - 1] > nums[mid]:
                    return nums[mid]
                elif nums[mid] >  nums[l]:
                    l = mid +1 
                else:
                    r = mid - 1
