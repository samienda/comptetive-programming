# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        

        idx = len(postorder) - 1

        def divide(inorder):
            nonlocal idx
            if not inorder:
                idx += 1
                return None

            center = postorder[idx]
            root = TreeNode(center)

            idx -= 1
            root.right = divide(inorder[inorder.index(center) + 1:])
            idx -= 1
            root.left = divide(inorder[:inorder.index(center)])

            return root

        return divide(inorder)
