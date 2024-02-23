# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def common(root):

            if p.val > root.val and q.val > root.val:
                return common(root.right)
                
            if p.val < root.val and q.val < root.val:
                return common(root.left)

            return root

        return common(root)

