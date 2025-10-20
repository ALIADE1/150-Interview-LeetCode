class Solution:
    def reverseDegree(self, s: str) -> int:
        ans, i = 0, 1

        for x in s:
            ans+= (26 - (ord(x) - ord('a'))) * i
            i+=1
            
        return ans
