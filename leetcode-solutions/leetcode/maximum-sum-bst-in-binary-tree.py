# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:    
        # return 0

        res = []
        def traverse(root):
            nonlocal res
            if not root:
                return 0, float('inf'), float('-inf')
            

            left, lmin, lmax = traverse(root.left)
            right, rmin, rmax = traverse(root.right)
            # print(left, [root.val], right)

            res.append(left)
            res.append(right)
            if (left and lmax >= root.val) or (right and rmin <= root.val):
                return -400000, -400000, 400000

            final = left + root.val + right
            return final, min(root.val, lmin, rmin), max(root.val, lmax, rmax)

        
        total, mini, maxi = traverse(root)
        if root and mini < root.val < maxi:
            res.append(total)
 
        return max(res)
            
        