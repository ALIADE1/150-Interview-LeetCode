class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""] * len(indices)

        for x in range(len(indices)):
            ans[indices[x]] = s[x]

        return "".join(ans)
