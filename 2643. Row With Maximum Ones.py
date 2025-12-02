class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n,m = len(mat), len(mat[0])
        max_row, max_cou = 0, 0

        for i in range(n):
            cou = 0
            for j in range(m):
                if mat[i][j] == 1:
                    cou+=1

            if cou > max_cou:
                max_cou = cou
                max_row = i

        return [max_row, max_cou]
