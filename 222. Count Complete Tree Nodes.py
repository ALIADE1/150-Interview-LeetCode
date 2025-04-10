# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        values = []
        def val(node):
            if not node:
                return
            val(node.left)
            values.append(node.val)
            val(node.right)
            return values
            
        val(root)
        return len(values)
