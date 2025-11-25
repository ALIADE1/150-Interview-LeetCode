class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxx = 0

        for x in sentences:
            x_list = x.split()
            maxx = max(maxx,len(x_list))

        return maxx
