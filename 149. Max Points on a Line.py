class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        max_points = 2
        for i in range(0,n):
            slopes = {}
            for j in range(i+1,n):
                dy = points[i][1] - points[j][1]
                dx = points[i][0] - points[j][0]

                if dx == 0:
                    slope = float('inf')
                else:
                    slope = dy/dx if dx !=0 else 0

                slopes[slope] = slopes.get(slope,0) + 1
                max_points = max(max_points, slopes[slope] + 1)

        return max_points
      
