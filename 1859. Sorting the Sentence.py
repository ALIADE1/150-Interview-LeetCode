class Solution:
    def sortSentence(self, s: str) -> str:
        list_words_split = s.split()
        ans = [""] * len(list_words_split)

        for x in list_words_split:
            x_index = int(x[-1])
            ans[x_index - 1] = x[:-1]

        return " ".join(ans)
