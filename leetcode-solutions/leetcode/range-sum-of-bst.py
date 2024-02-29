# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total = 0
        def inorder(root):
            nonlocal total
            if not root:
                return

            if low <= root.val <= high:
                total += root.val

            inorder(root.left)
            inorder(root.right)


        inorder(root)

        return total

        