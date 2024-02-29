# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(left, right):
            if not left and not right:
                return True
            
            if not (left and right):
                return False


            if left.val != right.val:
                return False

            one = traverse(left.left, right.right)
            two = traverse(left.right, right.left)

            return one and two

        return traverse(root.left, root.right)


        