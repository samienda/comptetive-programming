# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(root1, root2):
            if not root1:
                return root2
            node1 = root2
            node2 = root2
            if root2:
                root1.val += root2.val
                node1 = root2.left
                node2 = root2.right

            root1.left = merge(root1.left, node1)
            root1.right = merge(root1.right, node2)


            return root1

        return merge(root1, root2)