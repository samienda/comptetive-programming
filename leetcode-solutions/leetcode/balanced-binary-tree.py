# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.ans = True
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            # print(left, right)

            if abs(right - left) > 1:
                self.ans = False
                return 0 

            return max(left, right) + 1
        
        height(root)
        return self.ans 