class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        ans = []

        for x in li:
            ans.append(x[::-1])

        return " ".join(ans)
