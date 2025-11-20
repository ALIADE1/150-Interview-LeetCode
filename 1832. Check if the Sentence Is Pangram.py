class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sen = set(sentence)

        return True if 26 <= len(sen) else False
