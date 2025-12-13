class Solution:
    def finalString(self, s: str) -> str:
        str_ans = ""
        n = len(s)

        for x in range(n):
            if s[x] != 'i':
                str_ans+=s[x]
            else:
                str_ans = str_ans[::-1]

        return str_ans
