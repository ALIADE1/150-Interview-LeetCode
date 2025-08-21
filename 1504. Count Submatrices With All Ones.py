class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        matrixx = [0] * m
        ans = 0

        for i in range(n):
            for j in range(m):
                matrixx[j] =  matrixx[j] + 1 if mat[i][j] else 0

            for k in range(m):
                minn, kk = matrixx[k], k
                while kk >=0 and minn:
                    minn = min(minn,matrixx[kk])
                    ans+=minn
                    kk-=1
        return ans
