# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        total = 0
        def traverse(root, num):
            nonlocal total
            if not root:
                return

            num += str(root.val)
            if not (root.left or root.right):
                total += int(num)


            traverse(root.left, num)
            traverse(root.right, num)


        traverse(root, "")
        return total



