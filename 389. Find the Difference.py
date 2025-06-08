class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)

        for x,y in zip(s,t):
            if x!=y:
                return y
                
        return t[-1]
