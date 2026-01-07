class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0] * (n-2) for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                maxx = 0

                for ii in range(3):
                    for jj in range(3):
                        maxx = max(maxx, grid[i+ii][j+jj])

                ans[i][j] = maxx

        return ans
