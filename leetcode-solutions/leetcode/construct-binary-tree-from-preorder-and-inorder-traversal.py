# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inoder: List[int]) -> Optional[TreeNode]:
        
        idx = 0
        def divide(inorder):
            nonlocal idx
            if not inorder:
                idx -= 1
                return None

            center = preorder[idx]
            root = TreeNode(center)

            idx += 1
            root.left = divide(inorder[:inorder.index(center)])
            idx += 1 
            root.right = divide(inorder[inorder.index(center) + 1:])

            return root
        
        return divide(inoder) 