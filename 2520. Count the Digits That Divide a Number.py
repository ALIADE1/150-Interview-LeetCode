class Solution:
    def countDigits(self, num: int) -> int:
        stt = str(num)
        cou_ans = 0

        for x in stt:
            if num % int(x) == 0:
                cou_ans+=1

        return cou_ans
