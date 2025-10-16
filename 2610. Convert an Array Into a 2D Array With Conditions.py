class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        max_freq = max(freq.values()) 
        ans = [[] for _ in range(max_freq)]

        for num in nums:
            for row in ans:
                if num not in row:
                    row.append(num)
                    break

        return ans
