class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        # ans.append()
        i = 1

        for x in encoded:
            ans.append(x^ans[-1])

        return ans
