class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq_cou = Counter(nums)
        max_freq = max(freq_cou.values())
        c = 0

        for x, y in freq_cou.items():
            if y == max_freq:
                c+=1

        return c * max_freq
