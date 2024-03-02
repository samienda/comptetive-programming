# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        res = []
        def traverse(root):
            nonlocal res
            if not root:
                return []

            left = traverse(root.left)
            right = traverse(root.right)

            for num in left:
                res.append(abs(root.val - num))

            for num in right:
                res.append(abs(root.val - num))

            return left + right + [root.val]

        x = traverse(root)
        # print(x)

        return max(res)