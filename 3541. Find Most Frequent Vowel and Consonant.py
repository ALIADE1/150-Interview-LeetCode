class Solution:
    def maxFreqSum(self, s: str) -> int:
        cou = {}
        vo = {'a', 'e', 'i', 'o', 'u'}
        maxv, maxnv = 0, 0

        for x in s:
            cou[x] = cou.get(x,0) + 1

        for x, y in cou.items():
            if x in vo:
                maxv = max(maxv,y)
            else:
                maxnv = max(maxnv,y)

        return maxv + maxnv
