class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans_summ = 0
        n = len(mat)
        midd = n// 2

        for i in range(0,n):
            ans_summ+=mat[i][i]
            ans_summ+=mat[i][n - i - 1]

        return ans_summ - mat[midd][midd] if n % 2 == 1 else ans_summ
