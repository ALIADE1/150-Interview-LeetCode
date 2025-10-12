class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        n = len(pref)

        for x in range(1,n):
            ans.append(pref[x]^pref[x-1])
        
        return ans
