class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_row = set()
        set_col = set()
        n = len(matrix)
        m = len(matrix[0])

        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j] == 0:
                    set_row.add(i)
                    set_col.add(j)

        for x in set_row:
            for i in range(0,m):
                matrix[x][i] = 0

        for x in set_col:
            for i in range(0,n):
                matrix[i][x] = 0

        return matrix
      
