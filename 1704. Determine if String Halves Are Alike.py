class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        first, second = s[:n], s[n:]
        
        vowels = set("aeiouAEIOU")
        
        c1 = sum(1 for ch in first if ch in vowels)
        c2 = sum(1 for ch in second if ch in vowels)
        
        return c1 == c2
