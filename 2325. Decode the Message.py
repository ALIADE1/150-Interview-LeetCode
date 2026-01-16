class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapp = {' ' : ' '}
        decoded_ans = ''
        i = 0

        for x in key:
            if x != ' ' and x not in mapp:
                mapp[x] = chr(i+97)
                i+=1

        for x in message:
            decoded_ans+=mapp[x]

        return decoded_ans
