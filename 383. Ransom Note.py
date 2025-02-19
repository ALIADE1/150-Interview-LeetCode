class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rl = [0] * 26
        ml = [0] * 26

        for x in ransomNote:
            rl[ord(x) - ord('a')] += 1

        for x in magazine:
            ml[ord(x) - ord('a')] += 1

        for r,m in zip(rl,ml):
            if (r !=0 and r > m) or r > m:
                return False
            else:
                continue
        return True
      
