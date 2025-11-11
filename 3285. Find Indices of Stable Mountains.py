class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        n = len(height)

        for x in range(1, n):
            if height[x - 1] > threshold:
                ans.append(x)

        return ans
