class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix and not matrix[0]:
            return []

        n = len(matrix)
        m = len(matrix[0])
        top = 0
        down = n - 1
        right = m - 1
        left = 0
        ans = []

        while top <= down and left <= right:
            for x in range(left,right + 1):
                ans.append(matrix[top][x])
            top+=1

            for x in range(top,down + 1):
                ans.append(matrix[x][right])
            right-=1

            if top <= down:
                for x in range(right,left-1,-1):
                    ans.append(matrix[down][x])
                down-=1

            if left <= right:
                for x in range(down,top-1,-1):
                    ans.append(matrix[x][left])
                left+=1
                
        return ans
      
