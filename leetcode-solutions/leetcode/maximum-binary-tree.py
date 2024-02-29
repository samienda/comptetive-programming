# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        def divide(nums):
            if not nums:
                return None

            idx = nums.index(max(nums))

            return TreeNode(nums[idx], divide(nums[:idx]), divide(nums[idx + 1:]))

        return divide(nums)
        