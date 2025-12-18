class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cou = set(Counter(s).values())

        return len(cou) == 1
