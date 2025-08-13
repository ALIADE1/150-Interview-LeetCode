class Solution:
    def convertDateToBinary(self, date: str) -> str:
        li = date.split("-")
        ans = ""

        for x in li:
            x = int(x)
            ans+=str(bin(x)[2:]) + "-"
            
        return ans[:-1]
