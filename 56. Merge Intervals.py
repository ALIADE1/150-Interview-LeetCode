class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for inter in intervals:
            if not ans or inter[0] > ans[-1][1]:
                ans.append(inter)
            else:
                ans[-1][1] = max(ans[-1][1],inter[1])

        return ans
      
