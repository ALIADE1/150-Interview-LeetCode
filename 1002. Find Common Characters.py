class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt_fw = Counter(words[0])

        for w in words[1:]:
            cnt_fw &= Counter(w)

        return list(cnt_fw.elements())
