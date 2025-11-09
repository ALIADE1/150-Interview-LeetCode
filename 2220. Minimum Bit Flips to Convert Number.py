class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bb = start ^ goal

        return bin(bb).count('1')
