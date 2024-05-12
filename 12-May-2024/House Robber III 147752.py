# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(root, robbed):

            if not root:
                # print(consi)
                return 0


            # print(root.val)
            if robbed:
                return  dfs(root.left, False) + dfs(root.right, False)
               
            else:
                return max(
                    dfs(root.left, robbed) + 
                        dfs(root.right, robbed),

                    dfs(root.right, True ) + 
                        dfs(root.left, True ) + root.val,
                )

        return dfs(root, False)