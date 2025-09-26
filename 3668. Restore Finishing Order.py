class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []

        for x in order:
            if x in friends:
                ans.append(x)

        return ans
