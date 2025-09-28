class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    c = abs(i-j)
                    ans[i]+=c
        
        return ans
