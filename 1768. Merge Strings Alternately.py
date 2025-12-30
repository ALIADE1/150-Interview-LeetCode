class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""

        for x,y in zip(word1,word2):
            ans+=x
            ans+=y

        ans+= word1[len(word2):]
        ans+= word2[len(word1):]

        return ans
