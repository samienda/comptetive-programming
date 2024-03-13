# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []
        def inorder(root):
            nonlocal nums
            if not root:
                return None

            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        inorder(root)
        # print(nums)

        # return root
            

        def divide(nums):
            if not nums:
                return None
            
            mid = len(nums) // 2

            left = divide(nums[:mid])
            right = divide(nums[mid + 1:])

            return TreeNode(nums[mid], left, right)

        return divide(nums)