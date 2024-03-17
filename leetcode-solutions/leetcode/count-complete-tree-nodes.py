# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def count(root):
            if not root:
                return 0

            left = count(root.left)
            right = count(root.right)

            return left + 1 + right

        return count(root)
        