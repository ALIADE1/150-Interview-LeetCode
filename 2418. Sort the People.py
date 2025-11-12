class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name = list(zip(names,heights))
        name.sort(key=lambda x:x[1], reverse = True)
        
        ans = []
        for x, _ in name:
            ans.append(x)

        return ans
