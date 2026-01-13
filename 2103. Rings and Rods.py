class Solution:
    def countPoints(self, rings: str) -> int:
        check_volor = {'B', 'G', 'R'}
        dictt = {}
        n = len(rings)
        ans_cou = 0

        for x in range(1,n,2):
            dictt.setdefault(rings[x],[]).append(rings[x-1])

        for x,y in dictt.items():
            y = set(y)
            if check_volor == y:
                ans_cou+=1

        return ans_cou
