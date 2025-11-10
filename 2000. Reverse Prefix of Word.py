class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = ""
        n = len(word)

        for i in range(n):
            if word[i] == ch:
                ans = word[:i+1][::-1] + word[i+1:]
                break

        return ans if ans else word
