class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ma1 = []
        ma2 = []
        for x in s:
            ma1.append(s.index(x))
        for x in t:
            ma2.append(t.index(x))
        return ma1 == ma2
      
