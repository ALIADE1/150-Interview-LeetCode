# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def InOrderTraversal(node):
            if not node:
                return
            InOrderTraversal(node.left)
            values.append(node.val)
            InOrderTraversal(node.right)
        InOrderTraversal(root)

        n = len(values)
        min_diff = 1e5 + 1
        for x in range(0,n-1):
            min_diff = min(min_diff,values[x+1] - values[x])
        return min_diff
