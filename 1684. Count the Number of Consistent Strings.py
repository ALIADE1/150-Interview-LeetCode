class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0

        for x in words:
            b = True
            for c in x:
                if c not in allowed:
                    b = False
                    break
                else:
                    continue
            if b:
                ans+=1

        return ans
