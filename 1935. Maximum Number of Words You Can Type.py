class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans_cou = 0
        list_words = text.split()

        for x in list_words:
            b = True
            for y in brokenLetters:
                if y in x:
                    b = False
                    break
            if b:
                ans_cou+=1

        return ans_cou
