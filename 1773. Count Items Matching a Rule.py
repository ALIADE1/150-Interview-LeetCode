class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mapp = {'type': 0, 'color': 1, 'name': 2}
        ans = 0

        for x in items:
            if x[mapp[ruleKey]] == ruleValue:
                ans+=1
        
        return ans
