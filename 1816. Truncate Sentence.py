class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list_split = s.split()

        return " ".join(list_split[:k])
