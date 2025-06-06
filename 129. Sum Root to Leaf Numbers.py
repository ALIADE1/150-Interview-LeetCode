# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def calc(summ,node):
            if not node:
                return 0
            
            summ = summ*10 + node.val

            if not node.left and not node.right:
                return summ

            return calc(summ,node.right) + calc(summ,node.left)

        return calc(0,root)

