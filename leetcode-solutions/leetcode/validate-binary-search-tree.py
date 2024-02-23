# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def compare(root, mini, maxi):
            if not root:
                return True

            if not (mini < root.val < maxi):
                return False

            left  = compare(root.left, mini, root.val)
            right  = compare(root.right, root.val, maxi)


            return left and right


        return compare(root, float('-inf'), float('inf'))


                 
        