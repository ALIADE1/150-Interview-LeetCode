class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans_summ = 0
        n = len(mat)
        midd = n// 2 
        i_f, j_f = 0, 0
        i_r, j_r = n - 1, n - 1


        for i in range(0,n):
            ans_summ+=mat[i_f][j_f]
            ans_summ+=mat[i_r][j_r]
            i_f+=1
            j_f+=1
            i_r-=1
            j_r-=1

        return ans_summ - mat[midd][midd] if n % 2 == 1 else ans_summ
