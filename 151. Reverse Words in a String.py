class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        li = s.split()
        li = li [::-1]
        ss = ' '.join(li)
        return ss
